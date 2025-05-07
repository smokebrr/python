#  Controle de Estoque: Faça um controle de estoque com menu de entrada, saída e exibição.
qtd = 0
while True:
    print("------------------------------------------------------")
    print("digite 1 para digite um valor para tirar do estoque ")
    print("digite 2 para digite um valor para inserir no estoque ")
    print("digite 3 para ver quanto produtos tem em estoque ")
    print("digite 4 para sair")
    print("------------------------------------------------------")
    opcao = int(input("insira uma opcao: "))
    
    if opcao == 1:
        n = int(input("insira uma quantidade pra tirar do estoque: "))
        qtd -= n
    if opcao == 2:
        n = int(input("insira uma quantidade pra inserir no estoque: "))
        qtd += n
    if opcao == 3:
        print(qtd)
    if opcao == 4:
        break