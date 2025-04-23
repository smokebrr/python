        #Conversão de Temperatura: Faça um programa que converta uma temperatura de Celsius para Fahrenheit.
#Continue pedindo ao usuário para inserir uma nova temperatura em Celsius até que ele digite "sair".
n = 0
sair = ""
while sair != "sair":
    n = float(input("insira a temperatura em celsius: "))
    f = (n*1.8)+32
    print(f"temperatura em fahrenheit: {f}")
    sair = input("Digite sair para pausar: ")

    
