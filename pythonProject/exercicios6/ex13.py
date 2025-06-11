# Leia uma lista de números e crie uma nova lista apenas com os valores únicos (sem repetições).
numeros = [3,5, 9, 4, 10, 13, 14, 16, 18, 20]

numeros_unicos = []
for numero in numeros:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)

print(numeros_unicos)