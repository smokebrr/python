a = float(input("insira seu peso: "))
b = float(input("insira sua altura: "))
c = a/(b**2)

if c<=18.5:
    print("voce esta abaixo do peso")
elif c>=18.5 and c<=25:
    print("voce esta com peso normal")
elif c>25 and c <=30:
    print("voce esta acima do peso")
elif c>30:
    print("voce esta obeso")