meu_array = ["leet", "code", "casa", "abacate"]
x = "e"
array_resultado = []

for posicao, palavra in enumerate(meu_array):
    if x in palavra:
        array_resultado.append(posicao)

print(array_resultado)