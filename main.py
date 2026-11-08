biblioteca = []


def cadastrar_livro(titulo, autor, ano, categoria):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "categoria": categoria,
        "status_de_leitura": "Não iniciado",
    }

    biblioteca.append(livro)


def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        for livro in biblioteca:
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Categoria: {livro['categoria']}")
            print(f"Status: {livro['status_de_leitura']}")
            print("-------------------------")


def pesquisar_livro():
    titulo_pesquisa = input("Digite o título do livro que deseja pesquisar: ")
    encontrado = False
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo_pesquisa.lower():
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Categoria: {livro['categoria']}")
            print(f"Status: {livro['status_de_leitura']}")
            encontrado = True
    if not encontrado:
        print("Livro não encontrado na biblioteca.")


def solicitar_dados_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano do livro: ")
    categoria = input("Digite a categoria do livro: ")
    return titulo, autor, ano, categoria


while True:
    print(f"==== GERENCIADOR DE BIBLIOTECA ====\n\n")
    print(f"1 - Cadastrar livro\n")
    print(f"2 - Listar livros\n")
    print("3 - Pesquisar livro\n")
    print(f"4 - Sair\n\n")

    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:
        titulo, autor, ano, categoria = solicitar_dados_livro()
        cadastrar_livro(titulo, autor, ano, categoria)
        print("Livro cadastrado!")
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        pesquisar_livro()
    elif opcao == 4:
        print("Obrigado por utilizar o Gerenciador de Biblioteca!\nAté a próxima!")
        break
    else:
        print("Opção inválida")
