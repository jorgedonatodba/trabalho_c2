from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_saldo_qtd_mov_conta.sql") as f:
            self.query_relatorio_saldo_qtd_mov_conta = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_tipo_de_conta_por_cliente.sql") as f:
            self.query_relatorio_tipo_de_conta_por_cliente = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_movimentacoes.sql") as f:
            self.query_relatorio_movimentacoes = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_contas.sql") as f:
            self.query_relatorio_contas = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_itens_pedidos.sql") as f:
            self.query_relatorio_itens_pedidos = f.read()

    def get_relatorio_saldo_qtd_mov_conta(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_saldo_qtd_mov_conta))
        input("Pressione Enter para Sair do Relatório de Visão Geral de Contas")

    def get_relatorio_tipo_de_conta_por_cliente(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_tipo_de_conta_por_cliente))
        input("Pressione Enter para Sair do Relatório de Tipo de Contas Por Cliente")

    def get_relatorio_contas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_contas))
        input("Pressione Enter para Sair do Relatório de Contas")

    def get_relatorio_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("Pressione Enter para Sair do Relatório de Clientes")

    def get_relatorio_movimentacoes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_movimentacoes))
        input("Pressione Enter para Sair do Relatório de Movimentações")

    def get_relatorio_itens_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_itens_pedidos))
        input("Pressione Enter para Sair do Relatório de Itens de Pedidos")