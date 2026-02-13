montanhas = [1,2,3,4,5,6,7,8,9]
limite = 2
meu_dicionario = {}

for altura in montanhas:
    if montanhas[altura-1] > limite:
        meu_dicionario[altura] = "Estavel"

print(meu_dicionario)