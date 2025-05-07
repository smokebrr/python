#Controle de Votação: Faça um programa que permita cadastrar votos para 3 candidatos.
# Exibe contagem ao final quando for digitado "fim".

voto1 = 0
voto2 = 0
voto3 = 0
while True:
    print("------------------------------------------------------")
    print("digite 1 para votar no candidato 1 ")
    print("digite 2 para votar no candidato 1 ")
    print("digite 3 para votar no candidato 1 ")
    print("digite 4 para mostrar o resultado")
    print("------------------------------------------------------")
    opcao = int(input("insira uma opcao: "))
    
    if opcao == 1:
        voto1 =+1
    if opcao == 2:
        voto2 =+1
    if opcao == 2:
        voto3 =+1
    if opcao == 4:
        print(f"Quantidade de votos por candidato: \n Candidato 1 : {voto1} \n Candidato 2 : {voto2} \n Candidato 3 : {voto3}")
        break
        
                
