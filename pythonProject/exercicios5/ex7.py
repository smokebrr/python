# Conversor de Moeda: Crie um programa que converta uma quantia em dólares para euros.
# Continue pedindo ao usuário quantias em dólares para converter até que ele insira "0".
n = ""
while n!=0:
    n = float(input("insira um valor em dolar para ser convertido para euro: "))
    print(f"valor em euro:{n*0.88}")