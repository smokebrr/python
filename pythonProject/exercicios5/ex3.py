# Quantidade de valores: Conte quantos valores positivos, negativos e zeros foram digitados.
positivos = 0
negativos = 0
while True:
    n = float(input("insira um numero: "))
    if n == 0:
        print("zero")
    if n> 0:
        positivos += 1
        print(f"positivo: {positivos}")
    elif n < 0:
        negativos += 1
        print(f"negativos: {negativos}")