#Se a palavra for maior que 10 caracteres escreva de uma maneira resumida, 
#  onde mostra a primeira e a ultima letra e a distante de caracteres entre elas
minha_string = "localization"

if len(minha_string) > 10:
    print(f"{minha_string[0]}{len(minha_string) - 2}{minha_string[-1]}")
else:
    print(minha_string)
