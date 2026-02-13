nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
um_digito = 0
dois_digitos = 0

try:
    opcao = int(
        input(
            "Escolha entre: \n1 - Números de um dígito\n2 - Números de dois dígitos\n"
        )
    )
except ValueError:
    print("Por favor, digite um valor válido.")

for numero in nums:
    if numero < 10:
        um_digito += numero
    else:
        dois_digitos += numero


if opcao == 1:
    print(f"Os números de um dígito são: {um_digito}")
    print(f"Os números de dois dígitos são: {dois_digitos}")

    if um_digito > dois_digitos:
        print("Vencedor")
    else:
        print("Perdedor")
elif opcao == 2:
    print(f"Os números de dois dígitos são: {dois_digitos}")
    print(f"Os números de um dígito são: {um_digito}")

    if dois_digitos > um_digito:
        print("Vencedor")
    else:
        print("Perdedor")
