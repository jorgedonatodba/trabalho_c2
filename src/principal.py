from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_cliente import Controller_Cliente
from controller.controller_conta import Controller_Conta
from controller.controller_movimentacao import Controller_Movimentacao

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_conta= Controller_Conta()
ctrl_cliente = Controller_Cliente()
ctrl_movimentacao = Controller_Movimentacao()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_clientes()            
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_contas()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_movimentacoes()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_tipo_de_conta_por_cliente()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_saldo_qtd_mov_conta()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_cliente = ctrl_cliente.inserir_cliente()
    elif opcao_inserir == 2:
        nova_conta = ctrl_conta.inserir_conta()
    elif opcao_inserir == 3:
        nova_movimentacao = ctrl_movimentacao.inserir_movimentacao()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_clientes()
        cliente_atualizado = ctrl_cliente.atualizar_cliente()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_clientescontas()
        conta_atualizada = ctrl_conta.atualizar_conta()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_movimentacoes()
        mov_atualizado = ctrl_movimentacao.atualizar_movimentacao()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_clientes()
        ctrl_cliente.excluir_cliente()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_contas()
        ctrl_conta.excluir_conta()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_fornecedores()
        ctrl_movimentacao.excluir_movimentacao()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-5]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()