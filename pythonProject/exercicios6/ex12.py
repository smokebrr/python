# Substitua todos os números ímpares de uma lista por zero.
lista = [3,5, 9, 4, 10, 13, 14, 16, 18, 20]

for i in lista:
    if i % 2 != 0:
        lista.remove(i)
        lista.append(0)
print(lista)