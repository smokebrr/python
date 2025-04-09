# Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero.
for i in range(1,10):
    n = float(input("insira 10 numeros: "))
    if n == 0:
        print("zero")
    elif n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")