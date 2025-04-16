# Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero.
positivos = 0
negativos = 0
for i in range(1,10):
    n = float(input("insira 10 numeros: "))
    if n == 0:
        print("zero")
    elif n > 0:
        positivos += 1
        print(f"positivo: {positivos}")
    elif n < 0:
        negativos += 1
        print(f"negativos: {negativos}")
