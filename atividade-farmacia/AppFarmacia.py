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

    if temProduto is None:
        print("remedio não encontrado")
        return

    codigo, detalhes = temProduto

    if quantidadeProduto > detalhes["quant"]:
        print(f"temos apenas {detalhes['quant']} em estoque desse remedio")
        return

    vendido = farmacinha.atualizar_quantidade_em_estoque(
        nomeProduto, quantidade=quantidadeProduto
    )

    if vendido:
        print(f"Produto:{detalhes["desc"]}")
        print(f"Quantidade:{detalhes["quant"]}")
        print(f"Total: R${detalhes["preco"]*detalhes["quant"]}")
        print("venda completa!")
        return
    else:
        print('deu algum problema na venda')
        return

# while True:
#     farmacinha.menu()

#     opcao = input()

#     match opcao:
#         case '1':
#             cadastros()
#             break
#         case '2':
#             vender()
#             break
#         case _:
#             print("Saindo...")
#             break
