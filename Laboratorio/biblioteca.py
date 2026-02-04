import sys

# Dicionário de livros
livros = {}
emprestimos = []


# Função exibir menu
def exibir_menu():
    print("\n--- Biblioteca ---")
    print("1 - Adicionar livro")
    print("2 - Listar livro")
    print("3 - Remover livro")
    print("4 - Atualizar quantidade de livros")
    print("5 - Registrar empréstimo")
    print("6 - Exibir histórico de empréstimos")
    print("7 - Sair")


# Função para adicionar produto
def adicionar_livro():
    titulo = input("Digite o Titulo do Livro: ")

    try:
        quantidade = int(input("Digite os Exemplares do Livro: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")

    autor = input("Quem é o autor desse Livro: ")

    if titulo not in livros:
        livros[titulo] = {"Descrição": {"Autor": autor, "Quantidade": quantidade}}
        return f"Livro '{titulo}' adicionado com sucesso!"
    else:
        return f"Erro: {titulo} já cadastrado."


# Função para listar Livros
def listar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\n--- Lista de Livros ---")

    for titulo in livros:
        dados = livros[titulo]["Descrição"]
        autor = dados["Autor"]
        qtd = dados["Quantidade"]

        print(f"Título: {titulo} | Autor: {autor} | Qtd: {qtd}")


# Função para remover livros
def remover_produto(livros, titulo):
    titulo = input("Digite o título do livro a ser removido: ")
    if titulo in livros:
        del livros[titulo]
        return f"Livro '{titulo}' removido com sucesso!"
    else:
        return "Erro: Livro não encontrado."


# Função para atualizar quantidade
def atualizar_quantidade(livros):
    titulo = input("Digite o título do livro a ser atualizado: ")
    try:
        nova_qtd = int(input("Digite a nova quantidade: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    if titulo in livros:
        livros[titulo]["Descrição"]["Quantidade"] = nova_qtd
        return f"Quantidade do livro '{titulo}' atualizada para {nova_qtd}."
    else:
        return "Erro: Livro não encontrado."


# Função Emprestimo de Livros
def registrar_emprestimo():
    titulo = input("Digite o Titulo do Livro: ")

    if titulo not in livros:
        return f"Erro: {titulo} não cadastrado."
    elif livros[titulo]["Descrição"]["Quantidade"] <= 0:
        return f"Erro: {titulo} não disponível para empréstimo."
    else:
        livros[titulo]["Descrição"]["Quantidade"] -= 1

        for livro in emprestimos:
            if livro[0] == titulo:
                livro[1] += 1
            break
        else:
            emprestimos.append([titulo, 1])

        print(f"Empréstimo do livro '{titulo}' registrado com sucesso!")


# Função Historico de Empréstimos
def exibir_historico_emprestimos():
    if not emprestimos:
        return "Nenhum empréstimo registrado."
    else:
        print("\n--- Histórico de Empréstimos ---")
        for item in emprestimos:
            print(item)


def sair():
    print("Saindo...")
    sys.exit()


# Função escolha menu
def escolha_menu():
    try:
        escolha = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("Opção inválida. Digite um número.")
        return

    if escolha == 1:
        resultado = adicionar_livro()
        print(resultado)
    elif escolha == 2:
        listar_livros(livros)
    elif escolha == 3:
        resultado = remover_produto(livros)
        print(resultado)
    elif escolha == 4:
        resultado = atualizar_quantidade(livros)
        print(resultado)
    elif escolha == 5:
        resultado = registrar_emprestimo()
        print(resultado)
    elif escolha == 6:
        resultado = exibir_historico_emprestimos()
        print(resultado)
    elif escolha == 7:
        sair()
    else:
        print("Opção ainda não implementada ou inválida.")


while True:
    exibir_menu()
    escolha_menu()
