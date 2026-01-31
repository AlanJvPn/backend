
# Função para ler um número com tratamento de exceção
def ler_numero(mensagem):
    while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Por favor, insira um número.")

# Dicionário de operações usando funções lambda
operacoes = {
    1: ("Soma", lambda a, b: a + b),
    2: ("Subtração", lambda a, b: a - b),
    3: ("Multiplicação", lambda a, b: a * b),
    4: ("Divisão", lambda a, b: a / b)
}

while True:
    print("\n--- Calculadora ---\n")
    num1 = ler_numero("Insira o primeiro número: ")
    num2 = ler_numero("Insira o segundo número: ")

    # Exibição do menu usando list comprehension
    print("\nEscolha uma operação:")
    [print(f"{i} - {operacoes[i][0]}") for i in operacoes]

    # Escolha da operação
    try:
        escolha = int(input("\nDigite o número da operação desejada: "))
        if escolha not in operacoes:
            print("Escolha inválida.")
            continue
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue

    # Tratamento especial para divisão por zero
    if escolha == 4:
        while num2 == 0:
            print("Erro! Divisor não pode ser zero.")
            num2 = ler_numero("Insira outro número: ")

    # Cálculo do resultado
    resultado = operacoes[escolha][1](num1, num2)
    print(f"\nVocê escolheu: {operacoes[escolha][0]}")
    print(f"O resultado é: {resultado}")

    continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
    if continuar != "S":
        break