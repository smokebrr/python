# Solicite ao usuário um número e verifique se ele é par ou ímpar.
# Se o número for par, divida-o por 2 e exiba o resultado.
# Se o número for ímpar, multiplique-o por 3 e exiba o resultado.
n = int(input("insira um numero: "))
for i in range(1):
    if n %2 == 0:
        print(f"resultado: {n/2} ")
    else:
        print(f"resultado: {n*3} ")