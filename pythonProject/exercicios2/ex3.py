a = int(input("insira uma idade:"))
if a <= 12:
    print("classificado como crianca")
elif a >= 13 and a <= 17:
    print("classificado como adolescente")
elif a >= 18 and a <= 64:
    print("classificado como adulto")
elif a > 65:
    print("classificado como idoso")