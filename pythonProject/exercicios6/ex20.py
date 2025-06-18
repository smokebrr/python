#Desenvolva um menu de opções para gerenciar uma lista de tarefas: adicionar, remover, exibir e sair.
lista = ["adicionar","remover","exibir","sair"]
print(lista)
func = input("digite uma das opcoes: ")
tarefas = []

while True:
    if func == "sair":
        break
    if func == "adicionar":
        add = input("digite algo para adicionar na lista de tarefas")
        tarefas.append(add)
        func = input("digite uma das opcoes: ")

    if func == "exibir":
        print(tarefas)
        func = input("digite uma das opcoes: ")
    if func == "remover":
        rem = input("digite corretamente uma das tarefas ja cadastradas para remover")
        tarefas.remove(rem)
        func = input("digite uma das opcoes: ")
