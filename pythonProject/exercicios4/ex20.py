# Crie um programa que solicite ao usuário um número e informe se ele é primo ou não. Lembre-se de que um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
n = int(input("insira um numero: "))
cont = 0
for i in range(n,0,-1):
    if n%i==0:
        cont+=1
if cont>2:
     print("nao primo")
else: 
    print("primo")
