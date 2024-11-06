from cliente import Cliente
from medicamento import Medicamento


class Farmacia:
    """Construtor da classe medicamento"""

    def __init__(self, cnpj="", nome_fant=""):
        self.__cnpj = cnpj
        self.__nome_fantasia = nome_fant
        self.__estoque = dict()
        self.__clientes = dict()

    def get_nome(self):
        return self.__nome_fantasia

    def get_clientes(self):
        return self.__clientes

    def cadastrar_cliente(self):
        nome = input("Nome do cliente: ")
        cpf = input("Número do cpf: ")

        cliente = Cliente(nome, cpf)

        self.__clientes.append(cliente)

    def cadastrar_medicamento(self):
        cod = input("Código do medicamento: ")
        desc = input("Nome do medicamento: ")
        quant = int(input("Quantidade de medicamento: "))
        preco = float(input("Preço do medicamento: "))

        medicamento = Medicamento(cod, desc, quant,preco)
        
        self.__estoque.setdefault(cod,medicamento)


    def limpar_clientes(self):
        self.__clientes.clear()

    def relatorio_cliente(self):
        for key, value in self.__clientes:
            print(key, value)

    def relatorio_medicamento(self):
        for key, value in self.__estoque:
            print(key, value)
    
    def procurar_por_nome(self, nome):
        for codigo, detalhes in self.__estoque.items():
            if detalhes['nome'].lower() == nome.lower():  
                return codigo, detalhes
        return None
    
    def atualizar_quantidade_em_estoque(self, nome):
        for codigo, detalhes in self.__estoque.items():
            if detalhes['nome'].lower() == nome.lower():  
                detalhes['quant'] += 1
        return None
    
    def menu(self):
        text_menu = """          
        ====================================
                Farmácia Porto Saúde 	 
        ====================================
        1.Cadastrar
            1.Cliente
            2.Medicamento
        2.Efetuar venda
        3.Devolver medicamentos ao Laboratório
        4.Atualizar preços
        5.Relatório de Estoque
            1.	Listar medicamentos sem estoque
            2.	Listar medicamento com estoque
            3.	Gerar relatório de vendas
        6.	Sair
        ====================================
        Informe uma opção:"""
        print(text_menu)
