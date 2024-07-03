'''
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
'''

#Programa: salario3

nome = input("Nome do funcionário:")
salario = float(input("Salário:"))
ts = int(input("Tempo de serviço:"))
if salario <=2000:
    if ts<=5:
        abono = 1000.00
    else:
        abono = 1500.00
else:
    if ts <=8:
        abono = 1200.00
    else:
        abono = 1800.00
salarioTotal = salario + abono
print("Nome=", nome)
print("Salário total=", salarioTotal)

