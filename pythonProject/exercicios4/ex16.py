# Peça ao usuário um número N e exiba quantos números entre 1 e N são múltiplos de 3 ou 5.
n1 = 0
n = int(input("insira um numero: "))
for i in range(1,n+1):
    if i % 3 == 0 or i % 5 == 0:
        n1 += 1
print(n1)
