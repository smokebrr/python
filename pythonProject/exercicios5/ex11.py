# Simulador de Caixa Registradora: O usuário digita o preço e a quantidade de produtos até digitar “sair”.
# O Sistema mostra a quantidade de produtos e o valor final da compra.
cont = ""
valor = ""
while True:
    print("digite sair quando tiver finalizado a compra")
    cont = input("digite quantos produtos pegou: ")
    valor = input("digite o valor do produto: ")
    if valor != "sair" or cont != "sair":
     print(f"Este é o valor final da compra: {cont*valor}")
     break

