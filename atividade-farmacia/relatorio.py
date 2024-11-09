from datetime import datetime
from medicamento import Medicamento


class Relatorio:

    def registrar_venda(self, codigo: str, nome: str, quantidade: int, preco: float) -> None:
        total = quantidade * preco
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        log = (
            f"Data/Hora: {timestamp}\n"
            f"Codigo:{codigo}\n"
            f"Medicamento: {nome}\n"
            f"Quantidade: {quantidade}\n"
            f"Preço Unitário: R${preco:.2f}\n"
            f"Total da Venda: R${total:.2f}\n"
            "-----------------------------\n"
        )

        with open("vendas.txt", "a") as arquivo_log:
            arquivo_log.write(log)

        print("Venda registrada no arquivo de log com sucesso!!\n")

    def ler_registros(self):
        try:
            with open("vendas.txt", "r") as arquivo_log:
                conteudo = arquivo_log.read()

                if conteudo:
                    print("Histórico de Vendas:\n")
                    print(conteudo)
                else:
                    print("Não há vendas registradas no momento.")
        except FileNotFoundError:
            print("Arquivo de log não encontrado. Nenhuma venda foi registrada até agora.")

    def registrar_devolucao(self, medicamento: Medicamento):
        with open("devolucoes.txt", "a") as file:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            log_mensagem = (
                f"Data/Hora: {timestamp}\n"
                f"Código: {medicamento.get_codigo()}\n"
                f"Medicamento: {medicamento.get_descricao()}\n"
                f"Quantidade Devolvida: {medicamento.get_quantidade()}\n"
                "-----------------------------\n"
            )
            file.write(log_mensagem)

    def ler_codigos_devolucao(self):
        with open("codigos_para_devolucao.txt", "r") as file:
            codigos = [linha.strip() for linha in file]
        return codigos

    def carregar_medicamentos_do_arquivo(self) -> dict:
        estoque = {}

        with open("fake_medicamentos.txt", "r") as arquivo:
            for linha in arquivo:

                linha = linha.strip()
                if not linha:
                    continue
                
                dados = linha.split(",")
                if len(dados) != 4:
                    print(f"Formato inválido na linha: {linha}")
                    continue

                cod = dados[0].strip()
                desc = dados[1].strip()
                quant = int(dados[2].strip())
                preco = float(dados[3].strip())

                medicamento = Medicamento(cod, desc, quant, preco)
                estoque[cod] = medicamento

        return estoque

