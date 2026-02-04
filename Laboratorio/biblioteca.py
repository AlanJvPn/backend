import sys

# Dicionário de livros
livros = {}

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

            livros[titulo] = { 
                "Descrição": {
                "Autor": autor,
                "Quantidade": quantidade
                }
            }
            return f"Livro '{titulo}' adicionado com sucesso!"
        else:
            return f"Erro: {titulo} já cadastrado."

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
    elif escolha == 7:
        sair()
    else:
        print("Opção ainda não implementada ou inválida.")


while True:
    exibir_menu()
    escolha_menu()
