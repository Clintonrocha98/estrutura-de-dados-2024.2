from cliente import Cliente
from medicamento import Medicamento

class Farmacia:
    def __init__(self, cnpj="", nome_fant=""):
        "cnpj"
        self.__cnpj = cnpj
        self.__nome_fantasia = nome_fant
        self.__estoque = dict()
        self.__clientes = dict()

    def get_nome(self):
        return self.__nome_fantasia

    def get_clientes(self):
        return self.__clientes

    def get_estoque(self):
        return self.__estoque

    def cadastrar_cliente(self):
        nome = input("Nome do cliente: ")
        cpf = input("Número do cpf: ")

        ja_existe_cpf = self._ja_existe_cpf(cpf)

        if ja_existe_cpf:
            print("cpf já cadastrado")
            return
        
        cliente = Cliente(nome, cpf)

        self.__clientes.setdefault(cliente)

        print("cliente cadastrado com sucesso!")
    
    def _ja_existe_cpf(self,cpf):
        "VALIDAR SE JÁ EXISTE CPF CADASTRADO"
        for value in self.__clientes:
            if value.get_cpf() == cpf:
                return True
            else:
                return False
    
    def cadastrar_medicamento(self):
        cod = input("Código do medicamento: ")
        desc = input("Nome do medicamento: ")
        quant = int(input("Quantidade de medicamento: "))
        preco = float(input("Preço do medicamento: "))

        if self._ja_existe_codigo(cod):
            print("codigo já cadastrado")
            return

        medicamento = Medicamento(cod, desc, quant,preco)
        
        self.__estoque.setdefault(cod,medicamento)

    def _ja_existe_codigo(self,cod):
        "VALIDAR SE JÁ EXISTE CODIGO CADASTRADO"
        for value in self.__estoque:
            if value.get_codigo() == cod:
                return True
            else:
                return False

    def limpar_clientes(self):
        self.__clientes.clear()

    def relatorio_cliente(self):
        for value in self.__clientes:
            print(value)

    def atualizar_preco(self,percentual):
        """
        1 - passar por todo estoque
        2 - verificar se o codigo é impar
        3 - verificar se o valor é menor que 25
        4 - atualizar todos os medicamentos com o novo valor
        """
        for value in self.__estoque:
            if int(value.get_codigo())%2 != 0 or value.get_preco() <= 25:
                value.set_value(value.get_value() * (1 + percentual / 100))
                print("novo valor")
                print(value.get_value())

        pass

    def relatorio_medicamento(self):
        for key, value in self.__estoque:
            print(key, value)
    
    def _encontrar_item_por_nome(self, nome):
        """Método auxiliar para buscar um item no estoque pelo nome."""
        for codigo, detalhes in self.__estoque.items():
            if detalhes.get_descricao().lower() == nome.lower():
                return codigo, detalhes
        return None

    def procurar_por_nome(self, nome):
        """Busca um item pelo nome e retorna o código e os detalhes, ou None se não encontrar."""
        resultado = self._encontrar_item_por_nome(nome)
        if resultado is not None:
            codigo, detalhes = resultado
            return codigo, detalhes
        return None

    def atualizar_quantidade_em_estoque(self, nome, quantidade=1):
        """Atualiza a quantidade em estoque subtraindo o valor especificado (padrão: 1)."""
        resultado = self._encontrar_item_por_nome(nome)
        if resultado is not None:
            _, detalhes = resultado

            detalhes.set_quantidade(detalhes.get_quantidade - quantidade)

            return True  
        
        return False 
    
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
