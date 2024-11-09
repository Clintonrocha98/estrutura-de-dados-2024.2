from lista import Lista
from time import sleep

def menu ():
    texto_menu = ''' 
    ===================================
    1 - Inserir item na lista (início)
    2 - Inserir item na lista (fim)
    3 - Inserir item na lista (ordenado)
    4 - Pesquisar item na lista
    5 - Remover item da lista
    6 - Exibir itens da lista
    0 - Sair
    ===================================\n'''
    print(texto_menu)

item_menu = -1

lista = Lista()

# while (True):
#     menu()
#     item_menu = int(input("Escolha uma opção do menu: "))
#     if item_menu == 1:
#         nome = input(' informe o seu nome \n')
#         lista.inserir_inicio(nome)

#     elif item_menu == 2:
#         nome = input(' informe o seu nome \n')
#         lista.inserir_final(nome)

#     elif item_menu == 3:
#         nome = input(' informe o seu nome \n')
#         lista.inserir_ordenado(nome)

#     elif item_menu == 4:
#         nome = input(' informe o seu nome \n')
#         lista.remover(nome)

#     elif item_menu == 6:
#         lista.imprimir()

#     elif item_menu == 0:
#         print("Finalizando o programa.")
#         input("Pressione qualquer tecla para finalizar.\n")           
#         break

#     else:
#         print("Opção inválida.")


lista.inserir_final("1")
lista.inserir_final("a")
lista.inserir_final("b")
lista.inserir_final("c")
lista.inserir_final("d")
lista.inserir_final("e")
lista.imprimir()