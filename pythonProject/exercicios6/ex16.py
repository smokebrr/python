#Junte duas listas e remova os elementos repetidos.
lista1 = ["joao","maria"]
lista2 = ["maria","jose"]

lista1.extend(lista2)
sem = list(set(lista1))

print(sem)