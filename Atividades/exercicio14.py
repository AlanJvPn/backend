# Dada uma string s consistindo apenas dos caracteres 'a' e 'b',
# retorne verdadeiro se cada 'a' aparecer antes de cada 'b' na string.
# Caso contrário, retorne falso. Não pode ter "ba"

string = "abababababbabab"

if 'ba' not in string:
    print("Ta certo!")
else:
    print("Ta Errado")