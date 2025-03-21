saldo = 0
opcao = ""

while opcao != "sair":
    opcao = str(input(" \nsaque \ndeposito \nsair \nescolha uma opcao:"))


    if opcao == "saque":
        b = int(input("digita quanto voce quer sacar: "))
        if b > saldo:
            print("saldo insuficiente")
            print(f"saldo: {saldo}")
        else:
            saldo-= b
            print("sacado com sucesso")
            print(f"saldo: {saldo}")
    elif opcao=="deposito":
        c = int(input("digite quanto voce quer depositar: "))
        saldo += c
        print("\ndepositado com sucesso")
        print(f"saldo: {saldo}")
    elif opcao =="sair":
        break
