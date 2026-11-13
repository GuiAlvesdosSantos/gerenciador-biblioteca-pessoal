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
    while True:
        titulo = input("Digite o título do livro: ").strip()
        if titulo:
            break
        print("O título não pode ficar vazio!")
    while True:
        autor = input("Digite o autor do livro: ").strip()
        if autor:
            break
        print("O autor não pode ficar vazio!")
    while True:
        ano = input("Digite o ano do livro: ").strip()
        if ano and ano.isdigit():
            ano = int(ano)
            break
        print("Digite um ano válido, utilizando apenas números!")
    while True:
        categoria = input("Digite a categoria do livro: ").strip()
        if categoria:
            break
        print("A categoria não pode ficar vazia!")

    return titulo, autor, ano, categoria


def atualizar_status(livro):
    print(f"\nTitulo: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Ano: {livro['ano']}")
    print(f"Categoria: {livro['categoria']}")
    print(f"Status Atual: {livro['status_de_leitura']}")
    print("-------------------------")

    print("Escolha o novo status:")
    print("1 - Não iniciado")
    print("2 - Em andamento")
    print("3 - Concluído")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        livro["status_de_leitura"] = "Não iniciado"
        print("Status atualizado com sucesso!")
    elif opcao == "2":
        livro["status_de_leitura"] = "Em andamento"
        print("Status atualizado com sucesso!")
    elif opcao == "3":
        livro["status_de_leitura"] = "Concluído"
        print("Status atualizado com sucesso!")
    else:
        print("Opção inválida! O status não foi alterado.")


def selecionar_livro():
    titulo_pesquisa = input("Digite o título do livro que deseja atualizar: ")
    encontrado = False

    for livro in biblioteca:
        if livro["titulo"].lower() == titulo_pesquisa.lower():
            atualizar_status(livro)
            encontrado = True
            break
    if not encontrado:
        print("Livro não encontrado na biblioteca.")


def remover_livro():
    livro_remover = input("Digite o título do livro que deseja remover: ")
    encontrado = False
    for livro in biblioteca:
        if livro["titulo"].lower() == livro_remover.lower():
            print("Livro encontrado")
            biblioteca.remove(livro)
            print(f"O livro '{livro['titulo']}' foi removido com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print("Livro não encontrado na biblioteca.")


def mostrar_estatisticas():
    total_livros = 0
    nao_iniciados = 0
    em_andamento = 0
    concluidos = 0
    for livro in biblioteca:
        total_livros += 1
        if livro["status_de_leitura"] == "Não iniciado":
            nao_iniciados += 1
        elif livro["status_de_leitura"] == "Em andamento":
            em_andamento += 1
        elif livro["status_de_leitura"] == "Concluído":
            concluidos += 1
    if total_livros == 0:
        print("Não existem livros cadastrados.")
    else:
        print(f"Total de livros: {total_livros}")
        print(f"Total de livros não iniciados: {nao_iniciados}")
        print(f"Total de livros em andamento: {em_andamento}")
        print(f"Total de livros Concluídos: {concluidos}")


while True:
    print(f"==== GERENCIADOR DE BIBLIOTECA ====\n")
    print(f"1 - Cadastrar livro\n")
    print(f"2 - Listar livros\n")
    print(f"3 - Pesquisar livro\n")
    print(f"4 - Atualizar status\n")
    print(f"5 - Remover livro\n")
    print(f"6 - Mostrar estatísticas\n")
    print(f"7 - Sair\n")

    opcao = input("Escolha uma opção:").strip()
    if opcao.isdigit():
        opcao = int(opcao)
    else:
        print("Digite uma opção válida, utilizando apenas números!")
        continue
    if opcao == 1:
        titulo, autor, ano, categoria = solicitar_dados_livro()
        cadastrar_livro(titulo, autor, ano, categoria)
        print("Livro cadastrado!")
        atualizar_status(biblioteca[-1])
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        pesquisar_livro()
    elif opcao == 4:
        selecionar_livro()
    elif opcao == 5:
        remover_livro()
    elif opcao == 6:
        mostrar_estatisticas()
    elif opcao == 7:
        print("Obrigado por utilizar o Gerenciador de Biblioteca!\nAté a próxima!")
        break
    else:
        print("Opção inválida")
