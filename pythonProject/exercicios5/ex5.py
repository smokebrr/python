saldo = 1000

while saldo !=0:
    print("digite 1 para saque")
    print("digite 2 para deposito")
    print("digite 3 para sair")
    print("digite 4 para ver o saldo")
    opcao = int(input("digite uma opcao: "))
    if opcao == 1:
        b = int(input("digite quanto voce quer sacar: "))
        if b > saldo:
            print("saldo insuficiente")
            print(f"saldo: {saldo}")
        else:
            saldo-= b
            print("sacado com sucesso")
            print(f"saldo: {saldo}")
    elif opcao == 2:
        b = int(input("digite quanto voce quer depositar"))
        saldo+=b
        print(f"Saldo: {saldo}")
    elif opcao == 3:
        break
    elif opcao == 4:
        print(f"Saldo: {saldo}")