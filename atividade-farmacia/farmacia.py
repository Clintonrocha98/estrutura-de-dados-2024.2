from cliente import Cliente
from medicamento import Medicamento
from typing import Dict, Optional
from relatorio import Relatorio
from utilitario import limpar_terminal

class Farmacia:
    __relatorio = Relatorio()

    def __init__(self):
        self.__estoque: Dict[str, Medicamento] = dict()
        self.__clientes: Dict[str, Cliente] = dict()

    def display_cadastros(self) -> None:
        """
        1. lista as opções de cadastro\n
        2. pega os dados necessarios para o cadastro\n 
        """
        limpar_terminal()

        print("oq vc quer cadastrar?")
        print("1. cliente")
        print("2. medicamento")
        print("3. medicamentos em massa\n")

        op = input()

        match op:
            case "1":
                limpar_terminal()
                nome = input("Nome do cliente: ")
                cpf = input("Número do cpf: ")
                self.__cadastrar_cliente(nome, cpf)
            case "2":
                limpar_terminal()
                cod = input("Código do medicamento: ")
                desc = input("Nome do medicamento: ")
                quant = int(input("Quantidade de medicamento: "))
                preco = float(input("Preço do medicamento: "))
                self.__cadastrar_medicamento(cod, desc, quant, preco)
            case "3":
                self.__cadastro_de_medicamento_em_massa()
            case _:
                print("opção invalida")

    def display_venda_de_remedio(self) -> None:
        """
        1. pergunta o nome do remedio\n
        2. pergunta a quantidade quer quer comprar\n
        3. verifica se o medicamento já existe\n
        4. verifica se tem a quantidade em estoque\n
        5. reduz a quantidade do remedio em estoque\n
        6. informa a venda no arquivo vendas.txt\n
        """
        limpar_terminal()

        nome = input("qual o remedio vc quer comprar?(nome) ")
        quantidade = int(input("qual a quantidade? "))

        medicamento = self.__procurar_medicamento_pelo_nome(nome)

        if medicamento is None:
            print("remedio não encontrado")
            return

        if quantidade > medicamento.get_quantidade():
            print(f"temos apenas {medicamento.get_quantidade()} em estoque desse remedio")
            print("venda não efetuada!")
            return

        nova_quantidade_do_medicamento = medicamento.get_quantidade() - quantidade

        medicamento.set_quantidade(nova_quantidade_do_medicamento)

        self.__relatorio.registrar_venda(
            medicamento.get_codigo(),
            medicamento.get_descricao(),
            quantidade,
            medicamento.get_preco(),
        )
        print(f"Produto: {medicamento.get_descricao()}")
        print(f"Quantidade: {quantidade}")
        print(f"Total: R${(medicamento.get_preco() * quantidade):.2f}")

        print("venda completa!")

    def devolver_medicamento_para_laboratorio(self) -> None:
        """
        1. verifico os codigos no arquivo .txt\n
        2. veirifico se retornou algum codigo\n
        3. procuro pelo medicamento usando o codigo\n
        4. verifico se o medicamento existe no estoque\n
        5. faço registro de devolução\n
        6. zerar a quantiadade do medicamento no estoque
        """
        limpar_terminal()
        codigos = self.__relatorio.ler_codigos_devolucao()
        cont = 0
        if not codigos:
            print("nenhum codigo encontrado")
            return

        for cod in codigos:
            medicamento = self.__procurar_medicamento_pelo_codigo(cod)

            if medicamento is None:
                print(f"Não foi encontrado medicamento com o codigo: {cod} em estoque!")
                continue

            self.__relatorio.registrar_devolucao(medicamento)

            medicamento.set_quantidade(0)
            cont +=1
        print(f'Foram devolvidos {cont} remedios!!\n')

    def display_atualizacao_de_preco(self) -> None:
        """
        1. pergunta qual o percentual para atualização de preço\n
        2. verifica nos remedios em estoque:\n
        - se o codigo do remedio é impar\n
        - se o preço do remedio é menor que 25\n
        3. atualiza o valor do remedio\n
        """
        limpar_terminal()
        
        percentual = input("Qual o o percentual para atualizar o preço?")

        for medicamento in self.__estoque.values():
            if int(medicamento.get_codigo()) % 2 != 0 or medicamento.get_preco() <= 25:
                medicamento.set_preco(medicamento.get_preco() * (1 + int(percentual) / 100))
                print(f"Medicamento:{medicamento.get_descricao()} teve seu preço atualizado!!")
                print(f"Novo valor:R${medicamento.get_preco():.2f}")

    def display_relatorios(self) -> None:
        """
        1. lista as opções referente a relatorio de estoque\n
        2. chama o metodo referente ao relatorio escolhido
        """
        limpar_terminal()

        print("Relatiorio de Estoque")
        print("1. Listar medicamentos sem estoque")
        print("2. Listar medicamentos com estoque")
        print("3. Gerar relatorio de vendas")

        op = input()

        match op:
            case "1":
                self.__listar_medicamento_sem_estoque()
                print("fim do relatorio!")
            case "2":
                self.__listar_medicamento_com_estoque()
                print("fim do relatorio!")
            case "3":
                self.__relatorio_de_vendas()
            case _:
                print("opção invalida")
  
    def __cadastrar_cliente(self, nome: str, cpf: str) -> None:
        """
        1. verifica se cpf já foi cadastrado\n
        2. cadastra cliente
        """
        ja_existe_cpf = self.__ja_existe_cpf(cpf)

        if ja_existe_cpf:
            print("cpf já cadastrado")
            return

        cliente = Cliente(nome, cpf)

        self.__clientes.setdefault(cpf, cliente)

        print("cliente cadastrado com sucesso!")

    def __ja_existe_cpf(self, cpf: str) -> bool:
        """
        1. verifica se o cpf já esta cadastrado\n
        """
        for cliente in self.__clientes.values():
            if cliente.get_cpf() == cpf:
                return True
            else:
                return False

    def __cadastrar_medicamento(self, cod: str, desc: str, quant: int, preco: float) -> None:
        """
        1. verifica se o codigo esta cadastrado\n
        2. adiciona o medicamento no estoque 
        """
        if self.__ja_existe_codigo(cod):
            print("codigo já cadastrado")
            return

        medicamento = Medicamento(cod, desc, quant, preco)

        self.__estoque.setdefault(cod, medicamento)

    def __ja_existe_codigo(self, cod: str) -> bool:
        """
        1. verifica se o codigo informado já existe\n
        """
        for medicamento in self.__estoque.values():
            if medicamento.get_codigo() == cod:
                return True
            else:
                return False

    def __procurar_medicamento_pelo_nome(self, nome: str) -> Optional[Medicamento]:
        """
        Busca um medicamento pelo nome e retorna o código e o medicamento, ou None se não encontrar.
        """
        for medicamento in self.__estoque.values():
            if medicamento.get_descricao().lower() == nome.lower():
                return medicamento
        return None

    def __procurar_medicamento_pelo_codigo(self, codigo: str) -> Optional[Medicamento]:
        """Busca um medicamento pelo codigo e retorna o código e o medicamento, ou None se não encontrar."""
        for cod, medicamento in self.__estoque.items():
            if cod == codigo:
                return medicamento
        return None

    def __listar_medicamento_sem_estoque(self) -> None:
        """
        1. mostra todos os medicamentos cadastrado no estoque que tem a quantidade igual a 0 (zero)\n
        """
        for medicamento in self.__estoque.values():
            if medicamento.get_quantidade() == 0:
                print(medicamento)

    def __listar_medicamento_com_estoque(self) -> None:
        """
        1. mostra todos os medicamentos cadastrado no estoque que tem a quantidade maior que 0 (zero)\n
        """
        for medicamento in self.__estoque.values():
            if medicamento.get_quantidade() > 0:
                print(medicamento)

    def __relatorio_de_vendas(self) -> None:
        """
        1. faz a leitura do arquivo vendas.txt e mostra todas a vendas
        """
        self.__relatorio.ler_registros()

    def __cadastro_de_medicamento_em_massa(self)->None:
        limpar_terminal()
        novos_medicamentos = self.__relatorio.carregar_medicamentos_do_arquivo()
        cont = 0
        for medicamento in novos_medicamentos.values():
            self.__cadastrar_medicamento(
                medicamento.get_codigo(),
                medicamento.get_descricao(),
                medicamento.get_quantidade(),
                medicamento.get_preco())
            cont +=1
        print(f'Foram cadastrados {cont} novos medicamentos')

    def menu(self) -> None:
        text_menu = """          
        ====================================
                Farmácia Porto Saúde 	 
        ====================================
        1.Cadastrar
            1.Cliente
            2.Medicamento
            3.Cadastrar medicamento usando arquivo .txt
        2.Efetuar venda
        3.Devolver medicamentos ao Laboratório
        4.Atualizar preços
        5.Relatório de Estoque
            1.	Listar medicamentos sem estoque
            2.	Listar medicamento com estoque
            3.	Gerar relatório de vendas
        0.	Sair
        ====================================
        Informe uma opção:"""
        print(text_menu)
