#Peça um número ao usuário e exiba sua tabuada de 1 a 10, mas se for múltiplo de 3, substitua pelo texto "Multiplo de 3".

n = int(input("insira um numero: "))
for i in range(1,11):
    n1 = n*i
    if n1 % 3 == 0:
        print("Multiplo de 3")
    else:
        print(f"{n} x {i} = {n*i}")
    

