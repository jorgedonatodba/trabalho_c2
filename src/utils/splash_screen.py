from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_clientes = config.QUERY_COUNT.format(tabela="clientes")
        self.qry_total_contas = config.QUERY_COUNT.format(tabela="contas")
        self.qry_total_movimentacoes = config.QUERY_COUNT.format(tabela="movimentacoes")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = '''
        #        ANTHONY MAHYHAKER SILVA
        #        CIRO MASSARIOL DE ARAUJO
        #        IVIE ALVARINO FAÉ DE OLIVEIRA E SILVA
        #        PEDRO HENRIQUE SOSSAI CAMATA''' 

        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_clientes)["total_clientes"].values[0]

    def get_total_contas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_contas)["total_contas"].values[0]

    def get_total_movimentacoes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_movimentacoes)["total_movimentacoes"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #              SISTEMA DE GESTÃO BANCÁRIA                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - CLIENTES:         {str(self.get_total_clientes()).rjust(5)}
        #      2 - CONTAS  :         {str(self.get_total_contas()).rjust(5)}
        #      3 - MOVIMENTAÇÕES     {str(self.get_total_movimentacoes()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """