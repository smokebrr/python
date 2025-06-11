# Crie uma lista com 5 notas de alunos, calcule a média e diga quais alunos ficaram acima da média.
notas = []
for i in range(5):
    notas = int(input("Digite 5 notas: "))
soma = 0
for i in range(5):
    soma = soma + notas
media = soma/5
print(f"a media das notas eh {media}")
if media >= 6: 
    print("alunos acima da media")
else:
    print("alunos abaixo da media")