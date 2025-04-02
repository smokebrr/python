# Peça 5 notas ao usuário e calcule a média delas.

soma = 0
for i in range(5):
    n = int(input("insira uma nota: "))
    soma = soma + n

print(f"a media das notas eh {soma/5}")