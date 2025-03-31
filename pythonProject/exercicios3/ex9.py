# 9. Simulador de Compra em Loja Online
# O usuário escolhe um produto e o programa informa o preço.

produto = str(input("insira um produto: \n salgado \n doce \n detergente \n banana: \n "))

match produto:
    case "salgado":
            print("R$5,00")
    case "doce":
            print("R$3,00")
    case "detergente":
            print("R$7,00")
    case "banana":
            print("R$10,00")
    case _:
            print("opcao invalida")