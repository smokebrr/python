# Crie um programa que solicite ao usuário um número e informe se ele é primo ou não. Lembre-se de que um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
n = int(input("insira um numero: "))
for i in range(1,2):
    if n % 2 == 0:
        print("não é primo")
    else: print("é primo")