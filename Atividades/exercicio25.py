
from collections import Counter

meu_array = [1,2,0]
contador = 1
meu_dicionario = {}

meu_dicionario = Counter(sorted(meu_array))

while True:
    if contador in meu_dicionario:
        contador += 1
    else:
        meu_dicionario[contador] = 1
        print(meu_dicionario)
        break