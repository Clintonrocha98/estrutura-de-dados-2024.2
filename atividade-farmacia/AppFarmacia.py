from farmacia import *
from medicamento import *

farmacinha = Farmacia("12345", "24 Horas")


def cadastros():
    print("1. cliente")
    print("2. medicamento")

    op = input()

    if op == "1":
        farmacinha.cadastrar_cliente()
    elif op == "2":
        farmacinha.cadastrar_medicamento()


def vender():
    ##nome e quantidade que quer comprar?
    ## verifica se o medicamento existe
    ## verifica se existe a quantidade em estoque
    ## atualizar a quantidade de produtos em estoque
    ## finalizar com o total da compra
    nomeProduto = input("qual o remedio vc quer comprar?")
    quantidadeProduto = input("qual a quantidade?")
    temProduto = farmacinha.procurar_por_nome(nomeProduto)
    
    pass


farmacinha.cadastrar_medicamento()


# while True:
#     farmacinha.menu()

#     opcao = input()

#     match opcao:
#         case '1':
#             cadastros()
#         case '2':
#             pass
#         case _:
#             print("Saindo...")
#             break
