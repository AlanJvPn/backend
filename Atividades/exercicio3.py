# Aprovado,Reprovado ou Recuperação:
# Receba a média de um aluno e diga se ele foi aprovado (média>= 7)
# Recuperação (média <= 5) ou 
# Reprovadao (média < 5)

# 1. Receba a nota do aluno
media = float(input("Digite a média do aluno: "))

# 2. Verifique a média e mostre o resultado na tela
if media >= 7:
    print("Aluno APROVADO!")
elif media >= 5 and media < 7:
    print("Aluno em RECUPERAÇÃO.")
else:
    print("Aluno REPROVADO.")