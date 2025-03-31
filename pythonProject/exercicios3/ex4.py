# 4. Cálculo de Desconto por Categoria
# O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis), e o programa exibirá o percentual de desconto correspondente.

Produto = str(input("insira o tipo de produto: eletronico \n roupas \n alimentos \n moveis \n ")).lower()

match Produto:
    case "eletronico":
            print("o valor de desconto sera: 10%")
    case "roupas":
            print("o valor do desconto sera: 5%")
    case "alimentos":
            print("o valor do desconto sera: 3%")
    case "moveis":
            print("o valor do desconto sera: 5%")
    case _:
        print("opcao invalida")