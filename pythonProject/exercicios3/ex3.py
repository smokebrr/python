# 3. Sistema de Login Simples
# O programa deve pedir ao usuário que informe seu nome de usuário e, com base nisso, conceder um nível de acesso:
# Admin → Acesso total
# Professor → Acesso ao ambiente acadêmico
# Aluno → Acesso ao ambiente de estudos 

usuario = str(input("insira seu tipo de usuario: admin \n professor \n aluno ")).lower()

match usuario:
    case "admin":
        print("acesso total concedido")
    case "professor":
        print("acesso ao ambiente academico concedido")
    case "aluno":
        print("acesso ao ambiente de estudo concedido")
    case _:
        print("opcao invalida")
    

