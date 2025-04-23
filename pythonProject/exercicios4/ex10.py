#Solicite um número ao usuário e exiba o seu fatorial (n!).

n = int(input("insira um numero: "))
acum = 1
for i in range(1,n+1):
    acum *= i
print(acum)
    
