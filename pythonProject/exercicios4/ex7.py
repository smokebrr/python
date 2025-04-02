# Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.
n = int(input("insira um numero: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")