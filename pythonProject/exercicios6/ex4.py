# Some todos os elementos de uma lista de inteiros digitados pelo usuário.
numeros = []
for i in range(5):
    numeros = int(input("Digite 5 numeros: "))
soma = 0
for i in range(5):
    soma = soma + numeros
print(soma)