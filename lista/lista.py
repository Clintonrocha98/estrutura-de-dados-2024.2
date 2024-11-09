from no import No
import time

class Lista:

    def __init__(self):
        self.__head = None

    def get_head(self):
        return self.__head
    
    def set_head(self,head):
        self.__head = head

    def is_empty(self):
        return self.__head is None

    def inserir_inicio(self, nome):
        novo = No(nome)
        if self.is_empty():
            self.__head = novo
        else:
            novo.set_next(self.__head)
            self.set_head(novo)

    def inserir_final(self, nome):
        novo = No(nome)
        
        if self.is_empty():
            self.__head = novo
        else:
            aux = self.__head
            
            while aux.get_next():
                aux = aux.get_next()

            aux.set_next(novo)

    def inserir_ordenado(self, nome):
        pass
        # Implementar o método

    def busca_item(self, nome):
        pass
        # Implementar o método

    def remover(self, nome):
        pass
        # Implementar o método

    def imprimir(self):
        if self.is_empty():
            print("lista vazia!")
            return
        
        aux = self.__head

        while aux:
            if aux.get_next() is None:
                print(f"[{aux}]")
            else:
                print(f"[{aux}]->",end=" ") 
            aux = aux.get_next()
           
                