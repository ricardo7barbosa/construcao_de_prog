#Programa: Salário2

horas = int(input("Nº de horas:"))
nivel = int(input("Nível do professor:"))
if nivel == 1:
    sal = horas * 32.80
else:
    if nivel == 2:
        sal = horas * 44.15
    else:
        if nivel == 3:
            sal = horas * 52.11
        else:
            print("Nível Inválido")
            sal = 0
print("Salário =", sal)
