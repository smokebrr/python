# 6. Simulação de Atendimento Telefônico
# O usuário seleciona uma opção de atendimento telefônico:
# 1 - Suporte Técnico
# 2 - Financeiro
# 3 - Cancelamento
# 4 - Falar com um atendente

opcao = str(input("insira uma das opcoes para ser encaminhado: \n suporte \n financeiro \n cancelamento \n atendente"))

match opcao:
    case "suporte":
        print("encaminhado para o suporte tecnico")
    case "financeiro":
        print("encaminhado para o setor financeiro")
    case "cancelamento":
        print("encaminhado para o setor de cancelamento")
    case "atendente":
        print("encaminhado para o atendente")
    case _:
        print("opcao invalida")

