# Peça ao usuário três números: início, fim e passo e exiba a sequência correspondente.

a = int(input("insira o primeiro numero: "))
b = int(input("insira o segundo numero: "))
c = int(input("insira o terceiro numero: "))
for i in range(a,b,c):
    print(i)