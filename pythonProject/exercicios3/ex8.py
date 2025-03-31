# 8. Sistema de Reserva de Passagens
# O usuário escolhe um destino (São Paulo, Rio de Janeiro, Curitiba, Salvador) e recebe o valor da passagem.

opcao = str(input("insira uma das opcoes para saber o valor da passagem : \n SP \n RJ \n curitiba \n salvador: \n ")).lower()

match opcao:
    case "SP":
        print("o valor da passagem é R$2000")
    case "RJ":
        print("o valor da passagem é R$2300")
    case "curitiba":
        print("o valor da passagem é R$2500")
    case "salvador":
        print("o valor da passagem é R$17000")
    case _:
        print("opcao invalida")
        

