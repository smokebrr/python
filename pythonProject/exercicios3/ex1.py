# 1. Conversor de Moedas
#Implemente um conversor de moedas que permita ao usuário escolher entre Dólar (USD), Euro (EUR) e Libra (GBP) e converter um valor informado para Reais (BRL).

opcao = str(input("Digite uma das opcoes para realizar a conversao \n USD \n EUR \n GBP"))
valor = int(input("Digite um valor para conversao em BRL"))

match opcao:
    case "USD":
        print(f"USD: {valor*5.7}")
    case "EUR":
        print(f"EUR: {valor*6.1}")
    case "GBP":
        print(f"GBP: {valor*7.4}")
    case _:
        print(f"opcao invalida")
    