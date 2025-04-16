# Crie um programa que solicite ao usuário para inserir números e
# some esses números até que o usuário insira zero.
# Quando zero for inserido, o programa deve imprimir a soma total.

soma = 0

while True:
    n = int(input("insira um numero: "))
    soma += n
    if n == 0:
        break
print(soma)