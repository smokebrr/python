# 7. Calculadora Simples
# O usuário escolhe uma operação matemática (+, -, *, /) e insere dois números. O programa exibe o resultado.

opcao = str(input("escolha uma das opcoes para fazer o calculo \n + \n - \n * \n /: \n"))
n1 = int(input("insira um valor: "))
n2 = int(input("insira um valor: " ))

match opcao:
    case "+":
        print(n1+n2)
    case "-":
        print(n1-n2)
    case "*":
        print(n1*n2)
    case "/":
        print(n1/n2)
    case _:
        print("opcao invalida")
        