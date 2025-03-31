# 2 . Cálculo de Área de Figuras Geométricas
# Desenvolva um programa que permita ao usuário escolher entre calcular a área de um quadrado, retângulo ou triângulo e insira os valores necessários para o cálculo.

opcao = str(input("insira uma opcao para fazer o calculo da area: Quadrado \n Retangulo \n Triangulo: \n ")).lower()


match opcao:
    case "quadrado":
        valor = float(input("insira o valor do lado: "))
        print(f"o valor da area do quadrado é {valor**2}")
    case "retangulo":
        valor1 = float(input("insira o valor da base: "))
        valor2 = float(input("insira o valor da altura: "))
        print(f"a area do retangulo é: {valor1*valor2}")
    case "Triangulo":
        valor1 = float(input("insira o valor da base: "))
        valor2 = float(input("insira o valor da altura: "))
        print(f"a area do retangulo é: {(valor1*valor2)/2}")
    case _:
        print("opcao invalida")
        
    
   