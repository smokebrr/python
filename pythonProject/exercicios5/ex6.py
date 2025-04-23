#Média de Notas: Escreva um programa que continue pedindo ao usuário para inserir notas (0 a 10) 
#e calcule a média dessas notas. O programa deve parar quando o usuário digitar uma nota negativa.
n = 1
cont = 0
while n>0:
    n = float(input("insira uma nota: "))
    cont += 1
    a= n/cont
    print(f"{a}")
    