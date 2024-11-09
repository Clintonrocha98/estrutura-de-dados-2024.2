class No:
    def __init__(self, nome):
        self.__nome = nome
        self.__next = None

    def get_nome(self):
        return self.__nome

    def get_next(self):
        return self.__next

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_next(self, next):
        self.__next = next

    def __str__(self):
        return str(self.get_nome())
