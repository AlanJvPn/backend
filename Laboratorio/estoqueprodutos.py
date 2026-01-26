# Função para adicionar produto
def adicionar_produto(estoque, nome, quantidade, preco):
    nome = nome.strip()
    if nome in estoque:
        return f"Erro: Produto já cadastrado."
    else:
        estoque[nome] = {"quantidade": quantidade, "preço": preco}
        return f"Produto '{nome}' adicionado com sucesso!"

# Função para listar produtos
def listar_produtos(estoque):
    if not estoque:
        return "Nenhum produto cadastrado."
    else:
        resultado = ["Lista de produtos:"]
        for nome, dados in sorted(estoque.items(), key=lambda item: item[0].lower()):
            resultado.append(f"{nome}: Quantidade disponível - {dados['quantidade']} | Preço - R${dados['preço']:.2f}")
        return "\n".join(resultado)

# Função para remover produtos
def remover_produto(estoque, nome):
    nome = nome.strip()
    if nome in estoque:
        del estoque[nome]
        return f"Produto '{nome}' removido com sucesso!"
    else:
        return "Erro: Produto não encontrado."

# Função para atualizar quantidade
def atualizar_quantidade(estoque, nome, nova_qtd):
    nome = nome.strip()
    if nome in estoque:
        estoque[nome]["quantidade"] = nova_qtd
        return f"Quantidade do produto '{nome}' atualizada para {nova_qtd}."
    else:
        return "Erro: Produto não encontrado."

# Função exibir menu
def exibir_menu():
    return (
        "\n--- Menu de Estoque ---\n"
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade de produto\n"
        "5 - Sair\n"
    )

# Função principal
def main():
    estoque = {} # Dicionário para armazenar produtos
    while True:
        print(exibir_menu())

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
            print(adicionar_produto(estoque, nome, quantidade, preco))

        elif opcao == "2":
            print(listar_produtos(estoque))

        elif opcao == "3":
            nome = input("Digite o nome do produto a remover: ")
            print(remover_produto(estoque, nome))

        elif opcao == "4":
            nome = input("Digite o nome do produto: ")
            nova_qtd = int(input("Digite a nova quantidade: "))
            print(atualizar_quantidade(estoque, nome, nova_qtd))

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()