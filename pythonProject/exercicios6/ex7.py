#Faça um programa que leia 10 números e armazene em duas listas: uma com pares e outra com ímpares
lista = [3,5, 9, 4, 10, 13, 14, 16, 18, 20]
par = []
impar = []
for i in lista:
    if i % 2 == 0: 
        par.append(i)

    else:
        impar.append(i)
        
print(f"impar: {impar}\n e par: {par}")