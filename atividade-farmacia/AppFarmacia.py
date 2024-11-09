from farmacia import *
from medicamento import *

farm = Farmacia()

while True:
    farm.menu()

    opcao = input()

    match opcao:
        case "1":
            farm.display_cadastros()
        case "2":
            farm.display_venda_de_remedio()
        case "3":
            farm.devolver_medicamento_para_laboratorio()
        case "4":
            farm.display_atualizacao_de_preco()
        case "5":
            farm.display_relatorios()
        case _:
            print("Saindo...")
            break
