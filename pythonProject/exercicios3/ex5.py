# 5 . Tradutor de Cores
# O usuário informa uma cor em português (vermelho, azul, verde, amarelo), e o programa exibe sua tradução para inglês.

cor = str(input("insira uma opcao para a traducao: vermelho \n azul \n verde \n amarelo: \n ")).lower()

match cor:
    case "vermelho":
        print("red")
    case "azul":
        print("blue")
    case "verde":
        print("green")
    case "amarelo":
        print("yellow")
    case _:
        print("opcao invalida")