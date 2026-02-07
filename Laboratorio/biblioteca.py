def obter_dados_livro(titulo, autor, quantidade):
    return f"{titulo} {autor} {quantidade}"

def obter_quantidade_livro(valor):
    try:
        quantidade = int(valor)
        if quantidade < 0:
            return "Erro: Quantidade não pode ser negativa."
        return quantidade
    except ValueError:
        return "Por favor, insira um número válido para a quantidade."

def validar_livro_existe(livros, titulo):
    if titulo in livros:
        return True
    return f"Erro: O livro '{titulo}' não foi encontrado."

def adicionar_livro(livros, titulo, autor, quantidade):
    if validar_livro_existe(livros, titulo):
        return "Erro: Livro já cadastrado."
    livros[titulo] = {"autor": autor, "quantidade": quantidade}
    return f"Livro '{titulo}' adicionado com sucesso"

def listar_livros(livros):
    if not livros:
        return "Não há livros cadastrados."
    resultado = []
    for titulo, dados in sorted(livros.items()):
        resultado.append(f"Título: {titulo} | Qtd: {dados['quantidade']} | Autor: {dados['autor']}")
    return "\n".join(resultado)

def remover_livro(livros, titulo):
    if validar_livro_existe(livros, titulo):
        del livros[titulo]
        return f"Livro '{titulo}' removido com sucesso!"
    else:
        return f"Erro: O livro '{titulo}' não foi encontrado."

def atualizar_quantidade(livros, titulo, nova_quantidade):
    if validar_livro_existe(livros, titulo):
        livros[titulo]["quantidade"] = nova_quantidade
        return f"Quantidade de exemplares do livro '{titulo}' atualizada para {nova_quantidade}"
    else:
        return f"Erro: O livro '{titulo}' não foi encontrado."

def registrar_emprestimo(livros, emprestimos, titulo, quantidade_emprestada):
    if validar_livro_existe(livros, titulo):
        if livros[titulo].get("quantidade", 0) >= quantidade_emprestada:
            livros[titulo]["quantidade"] -= quantidade_emprestada
            emprestimos.append((titulo, quantidade_emprestada))
            return f"{quantidade_emprestada} exemplares de '{titulo}' emprestados com sucesso!"
        else:
            return "Erro: Estoque insuficiente."
    else:
        return f"Erro: O livro '{titulo}' não foi encontrado."

def obter_quantidade_livro_para_emprestimo(livros, titulo, valor):
    try:
        quantidade = int(valor)
        if quantidade <= 0:
            return "A quantidade deve ser maior que zero."
        elif quantidade > livros.get(titulo, {}).get("quantidade", 0):
            return "Erro: Quantidade solicitada maior que o estoque."
        else:
            return quantidade
    except ValueError:
        return "Erro: Entrada inválida."

def exibir_historico_emprestimos(emprestimos):
    if not emprestimos:
        return "Não há histórico de empréstimos."
    return "\n".join([f"Livro: {t} - Qtd: {q}" for t, q in emprestimos])

def exibir_menu():
    return (
        "\n--- Biblioteca ---\n"
        "1. Adicionar Livro\n"
        "2. Listar Livros\n"
        "3. Remover Livro\n"
        "4. Atualizar Quantidade\n"
        "5. Registrar Empréstimo\n"
        "6. Histórico de Empréstimos\n"
        "7. Sair"
    )

def menu():
    livros = {}
    emprestimos = []

    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            entrada_qtd = input("Quantidade: ")
            quantidade = obter_quantidade_livro(entrada_qtd)
            
            if isinstance(quantidade, int):
                print(adicionar_livro(livros, titulo, autor, quantidade))
            else:
                print(quantidade)
            
        elif opcao == "2":
            print(listar_livros(livros))
            
        elif opcao == "3":
            titulo = input("Título para remover: ")
            print(remover_livro(livros, titulo))
            
        elif opcao == "4":
            titulo = input("Título para atualizar: ")
            quantidade = int(input("Nova Quantidade: "))
            print(atualizar_quantidade(livros, titulo, quantidade))
            
        elif opcao == "5":
            titulo = input("Título do livro: ")
            entrada_qtd = input("Quantidade para empréstimo: ")
            quantidade_valida = obter_quantidade_livro_para_emprestimo(livros, titulo, entrada_qtd)
            
            if isinstance(quantidade_valida, int):
                print(registrar_emprestimo(livros, emprestimos, titulo, quantidade_valida))
            else:
                print(quantidade_valida)
                
        elif opcao == "6":
            print(exibir_historico_emprestimos(emprestimos))
            
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()