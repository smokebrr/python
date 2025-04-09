        #Peça um número ao usuário e exiba sua tabuada de 1 a 10, mas se for múltiplo de 3, substitua pelo texto "Multiplo de 3".

n = int(input("insira um numero: "))
for i in range(1,11):
    if (i%3)==0:
        print(f"multiplo de 3: {i}")
    else: 
        print(f"{i*n}")
