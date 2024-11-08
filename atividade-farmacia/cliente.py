class Cliente:
    num_clientes = 0

    def __init__(self, nome="", cpf=""):
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_cpf(self) -> str:
        return self.__cpf

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def atualiza_num_clientes(self) -> None:
        self.num_clientes += 1

    def get_num_clientes(self) -> int:
        return self.num_clientes

    def __str__(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}"
