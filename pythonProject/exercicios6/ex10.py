# Faça um programa que leia números do usuário até que ele digite 0. Depois, mostre a lista e a soma dos números.
lista = []
while True:
    n = int(input("insira um numero: "))
    lista.append(n)
    if n == 0:
        break
print(f"a soma é {sum(lista)}")
