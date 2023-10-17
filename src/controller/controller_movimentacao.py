from model.movimentacoes import Movimentacao
from model.contas import Conta
from controller.controller_conta import Controller_Conta
from conexion.oracle_queries import OracleQueries
from datetime import date

class Controller_Movimentacao:
    def __init__(self):
        self.ctrl_conta = Controller_Conta()
        
    def inserir_movimentacao(self) -> Movimentacao:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        
        # Lista os pedido existentes para inserir no item de pedido
        self.listar_contas(oracle, need_connect=True)
        lnumero = int(input("Digite o número da Conta: "))
        nconta = self.valida_conta(oracle, lnumero)
        if nconta == None:
            return None

        datamov = date
        tipomov = input("Informar o Tipo da Movimemtação (C)rédito ou (D)ébito: ")

        vvalor = float(input("Informar o Valor da Movimentação: "))

        if (vvalor.__lt__(0)):
            print("Valor inválido - não pode ser negativo")
            return None

        vcontaid = nconta.get_id()
        vcontasaldo = nconta.get_saldo()
        vcontalimite = nconta.get_limite()
        vnumeroconta = nconta.get_numero()
        vsaldoatu = 0

        if tipomov.upper() == 'C':
            vdesc = 'CREDITO EM CONTA'
            vsaldoant = vcontasaldo
            vsaldoatu = vcontasaldo + vvalor
        elif tipomov.upper() == 'D':
            vdesc = 'DÉBITO EM CONTA'
            vsaldoant = vcontasaldo
            vsaldoatu = vcontasaldo - vvalor
            vvalor = vvalor*-1
        else:
            print("Favor, informar (C)rédito ou (D)ébito.")
            return None

        if (vcontalimite*-1) <= vsaldoatu:
            # Cria uma nova conexão com o banco que permite alteração
            oracle = OracleQueries(can_write=True)
            oracle.connect()
            # Insere e persiste o novo saldo e movimento
            oracle.write(f"update contas set saldo = {vsaldoatu} where id = {vcontaid}",False)
            oracle.write(f"insert into movimentacoes values (seq_movimentacoes_id.nextval, '{datamov}', '{vdesc}', '{vvalor}', '{vsaldoant}', '{vsaldoatu}', '{vcontaid}')")
            # Recupera os dados do novo conta criado transformando em um DataFrame
            df_mov = oracle.sqlToDataFrame(f"select '{vnumeroconta}' as num,id, data, descricao, valor, saldo_anterior, saldo_atual from movimentacoes where id = seq_movimentacoes_id.curval")
            # Cria um novo objeto conta
            nova_mov = Movimentacao(df_mov.num.values[0], df_mov.data.values[0], df_mov.descricao.values[0], df_mov.valor.values[0], df_mov.saldo_anterior.values[0],df_mov.saldo_atual.values[0])
            # Exibe os atributos do novo conta
            print(nova_mov.to_string())
            # Retorna o objeto novo_conta para utilização posterior, caso necessário
            return nova_mov
        else:
            print(f"A Movimentação não pode ser executada - Conta {vnumeroconta} - Limite de {vcontalimite} excedido.")
            return None

        '''# Recupera o código do novo item de pedido
        codigo_movimentacao = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo item de pedido criado transformando em um DataFrame
        df_movimentacao = oracle.sqlToDataFrame(f"select codigo_movimentacao, quantidade, valor_unitario, codigo_pedido, codigo_produto from itens_pedido where codigo_movimentacao = {codigo_movimentacao}")
        # Cria um novo objeto Item de Pedido
        nova_movimentacao = ItemPedido(df_movimentacao.codigo_movimentacao.values[0], df_movimentacao.quantidade.values[0], df_movimentacao.valor_unitario.values[0], pedido, produto)
        # Exibe os atributos do novo Item de Pedido
        print(nova_movimentacao.to_string())
        # Retorna o objeto nova_movimentacao para utilização posterior, caso necessário
        return nova_movimentacao

    def atualizar_movimentacao(self) -> ItemPedido:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do item de pedido a ser alterado
        codigo_movimentacao = int(input("Código do Item de Pedido que irá alterar: "))        

        # Verifica se o item de pedido existe na base de dados
        if not self.verifica_existencia_movimentacao(oracle, codigo_movimentacao):

            # Lista os pedido existentes para inserir no item de pedido
            self.listar_pedidos(oracle, need_connect=True)
            codigo_pedido = str(input("Digite o número do Pedido: "))
            pedido = self.valida_pedido(oracle, codigo_pedido)
            if pedido == None:
                return None

            # Lista os produtos existentes para inserir no item de pedido
            self.listar_produtos(oracle, need_connect=True)
            codigo_produto = str(input("Digite o código do Produto: "))
            produto = self.valida_produto(oracle, codigo_produto)
            if produto == None:
                return None

            # Solicita a quantidade de itens do pedido para o produto selecionado
            quantidade = float(input(f"Informe a quantidade de itens do produto {produto.get_descricao()}: "))
            # Solicita o valor unitário do produto selecionado
            valor_unitario = float(input(f"Informe o valor unitário do produto {produto.get_descricao()}: "))

            # Atualiza o item de pedido existente
            oracle.write(f"update itens_pedido set quantidade = {quantidade}, valor_unitario = {valor_unitario}, codigo_pedido = {pedido.get_codigo_pedido()}, codigo_produto = {produto.get_codigo()} where codigo_movimentacao = {codigo_movimentacao}")
            # Recupera os dados do novo item de pedido criado transformando em um DataFrame
            df_movimentacao = oracle.sqlToDataFrame(f"select codigo_movimentacao, quantidade, valor_unitario, codigo_pedido, codigo_produto from itens_pedido where codigo_movimentacao = {codigo_movimentacao}")
            # Cria um novo objeto Item de Pedido
            movimentacao_atualizado = ItemPedido(df_movimentacao.codigo_movimentacao.values[0], df_movimentacao.quantidade.values[0], df_movimentacao.valor_unitario.values[0], pedido, produto)
            # Exibe os atributos do item de pedido
            print(movimentacao_atualizado.to_string())
            # Retorna o objeto pedido_atualizado para utilização posterior, caso necessário
            return movimentacao_atualizado
        else:
            print(f"O código {codigo_movimentacao} não existe.")
            return None

    def excluir_movimentacao(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do item de pedido a ser alterado
        codigo_movimentacao = int(input("Código do Item de Pedido que irá excluir: "))        

        # Verifica se o item de pedido existe na base de dados
        if not self.verifica_existencia_movimentacao(oracle, codigo_movimentacao):            
            # Recupera os dados do novo item de pedido criado transformando em um DataFrame
            df_movimentacao = oracle.sqlToDataFrame(f"select codigo_movimentacao, quantidade, valor_unitario, codigo_pedido, codigo_produto from itens_pedido where codigo_movimentacao = {codigo_movimentacao}")
            pedido = self.valida_pedido(oracle, df_movimentacao.codigo_pedido.values[0])
            produto = self.valida_produto(oracle, df_movimentacao.codigo_produto.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o item de pedido {codigo_movimentacao} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                # Revome o produto da tabela
                oracle.write(f"delete from itens_pedido where codigo_movimentacao = {codigo_movimentacao}")                
                # Cria um novo objeto Item de Pedido para informar que foi removido
                movimentacao_excluido = ItemPedido(df_movimentacao.codigo_movimentacao.values[0], df_movimentacao.quantidade.values[0], df_movimentacao.valor_unitario.values[0], pedido, produto)
                # Exibe os atributos do produto excluído
                print("Item do Pedido Removido com Sucesso!")
                print(movimentacao_excluido.to_string())
        else:
            print(f"O código {codigo_movimentacao} não existe.")

    def verifica_existencia_movimentacao(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados do novo pedido criado transformando em um DataFrame
        df_conta = oracle.sqlToDataFrame(f"select codigo_movimentacao, quantidade, valor_unitario, codigo_pedido, codigo_produto from itens_pedido where codigo_movimentacao = {codigo}")
        return df_conta.empty'''

    def listar_contas(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select c.numero
                ,c.tipo
                ,c.saldo
                ,c.limite
                from contas c
                order by c.numero
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_conta(self, oracle:OracleQueries, pnumero:int=None) -> Conta:
        if self.ctrl_conta.verifica_existencia_conta(oracle, pnumero):
            print(f"A Conta {pnumero} informada não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados da conta para o novo movimento criado transformando em um DataFrame
            df_conta = oracle.sqlToDataFrame(f"select id,  numero,  tipo,  saldo,  limite,  id_cliente from contas where numero = {pnumero}")
            # Cria um novo objeto cliente
            nconta = Conta(df_conta.id.values[0], df_conta.numero.values[0], df_conta.tipo.values[0], df_conta.saldo.values[0], df_conta.limite.values[0], df_conta.id_cliente.values[0])
            return nconta