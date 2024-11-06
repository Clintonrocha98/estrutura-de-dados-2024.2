class Medicamento:

    def __init__(self, cod = "", desc = "", quant = 0, preco = 0.0 ):
        self.__codigo = cod
        self.__descricao = desc
        self.__quantidade = quant
        self.__preco = preco

    def get_codigo(self):
        return self.__codigo
    
    def get_descricao(self):
        return self.__descricao
    
    def get_quantidade(self):
        return self.__quantidade
    
    def get_preco(self):
        return self.__preco

    def set_codigo(self, codigo):
        self.get_codigo = codigo
    
    def set_descricao(self, desc):
        self.get_descricao = desc
    
    def set_quantidade (self, quant):
        self.__quantidade = quant

    def set_preco(self, novo_preco):
        self.__preco = novo_preco

    def __str__(self):
        return f'Código: {self.__codigo}\nDescrição: {self.__descricao}\n'\
                f'Quantidade: {self.__quantidade}\nPreço: {self.__preco}'