# Simulação de Dados de Sensor: Crie um programa que simule a leitura de dados de um sensor e
# continue capturando dados até que um valor fora do intervalo de operação seja detectado 
# por exemplo, fora de 0 a 100).
n = ""
while n > 100 or n < 0:
    n = float(input("insira o valor do sensor: "))