meu_array = [1,2,3,4,5,5,6,7,8,9,9]

meu_dicionario = {}
novo_array = []
for numero in meu_array:
    if numero not in meu_dicionario:
        meu_dicionario[numero] = 1
    else:
        meu_dicionario[numero] += 1

print(meu_dicionario)

for chave, valor in meu_dicionario.items():
    if valor > 1:
        novo_array.append(chave)
        meu_array.remove(chave)

print(meu_array)
print(novo_array)