#Simule um carrinho de compras: adicione produtos até que o usuário digite 'fim' e, no final, mostre o carrinho.

lista = input("insira produtos, e quando quiser parar,digite 'fim':  ")
lista1 = []
while True:
    lista = input("insira produtos, e quando quiser parar,digite 'fim':  ")
    if lista == "fim":
        break
    else:
        lista1.append(lista)

print(lista1)



