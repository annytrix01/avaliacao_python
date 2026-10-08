class Documento:

    # Atributos privados
    def __init__(self, titulo, conteudo, tipo):
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__tipo = tipo

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_tipo(self):
        return self.__tipo


class Impressora:

    # Relação de dependência: usa o documento apenas para imprimir
    def imprimir(self, documento):
        print("\n--- DOCUMENTO ---")
        print("Título:", documento.get_titulo())
        print("Tipo:", documento.get_tipo())
        print("Conteúdo:", documento.get_conteudo())


impressora = Impressora()
documento = None


# Menu principal
while True:

    print("\n===== MENU =====")
    print("1 - Criar documento")
    print("2 - Imprimir documento")
    print("3 - Sair")
    print("================\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título: ")
        conteudo = input("Digite o conteúdo: ")
        tipo = input("Digite o tipo: ")

        documento = Documento(titulo, conteudo, tipo)
        print("Documento criado com sucesso!")

    elif opcao == "2":
        if documento is not None:
            impressora.imprimir(documento)
        else:
            print("\nNenhum documento foi criado.")

    elif opcao == "3":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida.")