a = int(input("insira um numero: "))
b = int(input("insira um numero: "))
c = str(input("insira se voce quer fazer uma adicao(+),uma divisao(/), uma subtracao(-) ou uma multiplicacao(*), com os numeros inseridos: "))

if c == "+":
    d=a+b
elif c== "-":
    d=a-b
elif c == "/":
    d=a/b
elif c == "*":
    d=a*b

print(f"o valor da operacao vai dar: {d}")