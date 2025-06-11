# Verifique se um nome digitado pelo usuário está em uma lista de nomes.

nomes = ["maria", "joao", "pedro", "jose", "marcelo"]
print(nomes)
nome = str(input("Digite um nome: "))
if nome in nomes:
    print("O nome esta na lista")
else:
    print("O nome nao esta na lista")