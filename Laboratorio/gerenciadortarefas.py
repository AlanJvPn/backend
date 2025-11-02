# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(string):
    nome = string.strip()
    if nome in tarefas:
        return "Essa tarefa já existe."
    else:
        tarefas[nome] = False
        return f"Tarefa '{nome}' adicionada com sucesso!!"

def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = []
        for nome, status in sorted(tarefas.items(), key=lambda item: item[0].lower()):
            status_emoji = "✅" if status else "❌"
            resultado.append(f"{status_emoji} {nome}")
        return "\n".join(resultado)

def remover_tarefa(nome):
    nome = nome.strip()
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."

def marcar_concluida(nome):
    nome = nome.strip()
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída!"
    else:
        return "Erro: Tarefa não encontrada."

def exibir_menu():
    return (
        print("\nMenu:"),
        print("1 - Adicionar tarefa"),
        print("2 - Listar tarefas"),
        print("3 - Remover tarefa"),
        print("4 - Marcar tarefa como concluída"),
        print("5 - Sair"),
    )

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome da tarefa: ").strip()
            print(adicionar_tarefa(nome))
        elif opcao == "2":
            print(listar_tarefas(tarefas))
        elif opcao == "3":
            nome = input("Nome da tarefa a remover: ").strip()
            print(remover_tarefa(nome))
        elif opcao == "4":
            nome = input("Nome da tarefa a marcar como concluída: ").strip()
            print(marcar_concluida(nome))
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()