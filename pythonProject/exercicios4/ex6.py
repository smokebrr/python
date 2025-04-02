# Solicite um número ao usuário e exiba a soma de 1 até esse número.
soma=0
n = int(input("insira um numero: "))
for i in range(1,n+1):
    print(i)
    soma = i +1
    print(f"soma= {soma}")

