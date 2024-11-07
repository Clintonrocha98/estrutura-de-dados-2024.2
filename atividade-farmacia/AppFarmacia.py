from farmacia import *
from medicamento import *

farmacinha = Farmacia("12345", "24 Horas")

def cadastros():
    print("oq vc quer cadastrar?")
    print("1. cliente")
    print("2. medicamento")

    op = input()

    match op:
        case "1":
            farmacinha.cadastrar_cliente()
        case "2":
            farmacinha.cadastrar_medicamento()
        case _:
            print("opção invalida")

def vender():
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
        nomeProduto, 
        quantidade=quantidadeProduto
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

while True:
    farmacinha.menu()

    opcao = input()

    match opcao:
        case '1':
            cadastros()
        case '2':
            vender()
        case "4":
            farmacinha.atualizar_preco()
        case _:
            print("Saindo...")
            break
