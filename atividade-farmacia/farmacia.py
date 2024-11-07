from cliente import Cliente
from medicamento import Medicamento
from typing import Dict, Optional


class Farmacia:
    def __init__(self, cnpj: str, nome_fant: str):
        "cnpj"
        self.__cnpj: str = cnpj
        self.__nome_fantasia: str = nome_fant
        self.__estoque: Dict[str, Medicamento] = dict()
        self.__clientes: Dict[str, Cliente] = dict()

    def cadastrar_cliente(self, nome: str, cpf: str) -> None:
        ja_existe_cpf = self._ja_existe_cpf(cpf)

        if ja_existe_cpf:
            print("cpf já cadastrado")
            return

        cliente = Cliente(nome, cpf)

        self.__clientes.setdefault(cpf, cliente)

        print("cliente cadastrado com sucesso!")

    def _ja_existe_cpf(self, cpf: str) -> bool:
        "Valida se o cpf já foi cadastrado!"
        for cliente in self.__clientes.values():
            if cliente.get_cpf() == cpf:
                return True
            else:
                return False

    def cadastrar_medicamento(
        self, cod: str, desc: str, quant: int, preco: float
    ) -> None:
        if self._ja_existe_codigo(cod):
            print("codigo já cadastrado")
            return

        medicamento = Medicamento(cod, desc, quant, preco)

        self.__estoque.setdefault(cod, medicamento)

    def _ja_existe_codigo(self, cod: str) -> bool:
        "valida se o codigo já foi cadastrado"
        for medicamento in self.__estoque.values():
            if medicamento.get_codigo() == cod:
                return True
            else:
                return False

    def limpar_clientes(self) -> None:
        self.__clientes.clear()

    def relatorio_cliente(self) -> None:
        for cliente in self.__clientes.values():
            print(f"cliente: {cliente}")

    def atualizar_preco(self, percentual: float) -> None:
        for medicamento in self.__estoque.values():
            if int(medicamento.get_codigo()) % 2 != 0 or medicamento.get_preco() <= 25:
                medicamento.set_preco(medicamento.get_preco() * (1 + percentual / 100))
                print(f"codigo:{medicamento.get_descricao()} preço atualizado!!")

    def relatorio_medicamento(self) -> None:
        for medicamento in self.__estoque.values():
            print(f"medicamento:{medicamento}")

    def procurar_medicamento_pelo_nome(self, nome: str) -> Optional[Medicamento]:
        """Busca um medicamento pelo nome e retorna o código e os detalhes, ou None se não encontrar."""
        for medicamento in self.__estoque.values():
            if medicamento.get_descricao().lower() == nome.lower():
                return medicamento
        return None

    def atualizar_quantidade_em_estoque(self, nome: str, quantidade=1) -> bool:
        """Atualiza a quantidade em estoque subtraindo o valor especificado (padrão: 1)."""
        resultado = self.procurar_medicamento_pelo_nome(nome)
        if resultado is not None:
            resultado.set_quantidade(resultado.get_quantidade - quantidade)

            return True

        return False

    def menu(self) -> None:
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
