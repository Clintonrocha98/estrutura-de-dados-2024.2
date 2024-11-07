from farmacia import *
from medicamento import *
import os


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


farmacinha = Farmacia("12345", "24 Horas")


def cadastros():
    print("oq vc quer cadastrar?")
    print("1. cliente")
    print("2. medicamento")

    op = input()

    match op:
        case "1":
            nome = input("Nome do cliente: ")
            cpf = input("Número do cpf: ")
            farmacinha.cadastrar_cliente(nome, cpf)
        case "2":
            cod = input("Código do medicamento: ")
            desc = input("Nome do medicamento: ")
            quant = int(input("Quantidade de medicamento: "))
            preco = float(input("Preço do medicamento: "))
            farmacinha.cadastrar_medicamento(cod, desc, quant, preco)
        case _:
            print("opção invalida")


def vender():
    nomeProduto = input("qual o remedio vc quer comprar?(nome)")
    quantidadeProduto = input("qual a quantidade?")
    medicamento = farmacinha.procurar_medicamento_pelo_nome(nomeProduto)

    if medicamento is None:
        print("remedio não encontrado")
        return

    if quantidadeProduto > medicamento["quant"]:
        print(f"temos apenas {medicamento.get_quantidade()} em estoque desse remedio")
        return

    vendido = farmacinha.atualizar_quantidade_em_estoque(
        nomeProduto, quantidade=quantidadeProduto
    )

    if vendido:
        print(f"Produto:{medicamento.get_descricao()}")
        print(f"Quantidade:{medicamento.get_quantidade()}")
        print(f"Total: R${medicamento.get_preco() * medicamento.get_quantidade()}")
        print("venda completa!")
        return
    else:
        print("deu algum problema na venda")
        return


def relatorios():
    print("Relatiorio de Estoque")
    print("1 - Listar medicamentos sem estoque")
    print("2 - Listar medicamentos com estoque")
    print("3 - Gerar relatorio de vendas")

    op = input()

    match op:
        case "1":
            print("em desenvolvimento")
        case "2":
            farmacinha.relatorio_medicamento()
        case "3":
            print("em desenvolvimento")
        case _:
            print("opção invalida")
    pass


while True:
    farmacinha.menu()

    opcao = input()

    match opcao:
        case "1":
            limpar_terminal()
            cadastros()
        case "2":
            limpar_terminal()
            vender()
        case "3":
            limpar_terminal()
            print("funcionalidade em desenvolvimento")
        case "4":
            limpar_terminal()
            percentual = input("Qual o o percentual para atualizar o preço?")
            farmacinha.atualizar_preco(float(percentual))
        case "5":
            limpar_terminal()
            relatorios()
        case _:
            print("Saindo...")
            break
