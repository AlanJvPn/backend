# Variavel Global

produtos = {}

# Função para adicionar produto

def adicionar_produto(): 
    nome = input("Digite o nome do produto: ").strip() 
    if nome in produtos:
        print("Produto já existe no estoque!") 
        return 
    try: 
        quantidade = int(input("Digite a quantidade: ")) 
        preco = float(input("Digite o preço: ")) 
        produtos[nome] = {"quantidade": quantidade, "preço": preco} 
        print(f"Produto '{nome}' adicionado com sucesso!") 
    except ValueError: 
        print("Erro: quantidade deve ser número inteiro e preço deve ser número decimal.") 
    
# Função para listar produtos

def listar_produtos(): 
    if not produtos: 
        print("Estoque vazio.") 
        return 
    print("\n--- Lista de Produtos ---") 
    for nome in sorted(produtos.keys(), key=lambda x: x.lower()): 
        print(f"{nome}: Quantidade disponível - {produtos[nome]['quantidade']} | Preço - R${produtos[nome]['preço']:.2f}") 
        print("-------------------------\n")
    
# Função para remover produtos

def remover_produto(nome):
    nome = nome.strip()
    if nome in produtos:
        del produtos[nome]
        return f"Produto '{nome}' removida com sucesso!"
    else:
        return "Erro: Produto não encontrada."

# Função para atualizar quantidade

def atualizar_quantidade(): 
    nome = input("Digite o nome do produto: ").strip() 
    if nome in produtos: 
        try: 
            nova_quantidade = int(input("Digite a nova quantidade: ")) 
            produtos[nome]["quantidade"] = nova_quantidade 
            print(f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}.") 
        except ValueError: 
            print("Erro: a quantidade deve ser um número inteiro.") 
    else: 
            print("Erro: produto não encontrado no estoque.")

# Função exibir menu

def exibir_menu():
    return (
        print("\nMenu:"),
        print("1 - Adicionar Produto"),
        print("2 - Listar Produtos"),
        print("3 - Remover Produto"),
        print("4 - Atualizar Quantidade do Produto"),
        print("5 - Sair"),
    )

# Função principal

def menu():
    while True:
        print("\n--- Menu de Estoque ---") 
        print("1 - Adicionar produto") 
        print("2 - Listar produtos") 
        print("3 - Remover produto") 
        print("4 - Atualizar quantidade de produto") 
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            nome = input("Nome do produto a remover: ").strip()
            print(remover_produto(nome))
        elif opcao == "4":
            atualizar_quantidade()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
menu()