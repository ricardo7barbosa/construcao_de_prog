#Programa: Salário

horas = int(input("Nº de horas:"))
nivel = int(input("Nível do professor:"))
if nivel == 1:
    sal = horas * 32.80
if nivel == 2:
    sal = horas * 44.15
if nivel == 3:
    sal = horas * 52.11
print("Salário =", sal)
