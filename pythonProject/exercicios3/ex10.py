# 10. Sistema de Pagamento
# O usuário escolhe uma forma de pagamento e o programa informa se há desconto ou acréscimo.

opcao = str(input("Insira uma forma de pagamento: \n PIX \n CREDITO : \n")).lower()

match opcao:
    case "pix":
        print("desconto de 10%")
    case "credito":
        print("juros de 10%")
    case _:
        print("opcao invalida")