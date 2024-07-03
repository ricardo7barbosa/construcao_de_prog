'''
#Programa: Salário3

horas = int(input("Nº de horas:"))
nivel = int(input("Nível do professor:"))
if nivel == 1:
    sal = horas * 32.80
elif nivel == 2:
    sal = horas * 44.15
elif nivel == 3:
    sal = horas * 52.21
else:
    print("Nível Inválido:")
    sal = 0
print("Salário =", sal)
'''
'''
#Program:Saúde

dep = int(input("Dependentes:"))
plano = int(input("Plano:"))
if plano == 1:
    valor = dep*320.00
elif plano == 2:
    valor = dep*260.00
elif plano == 3:
    valor = dep*215.00
elif plano == 4:
    valor = dep*148.00
else:
    print("Plano inválido")
    valor = 0
print("Total =", valor)
'''

'''
#Programa:KW/H

qtdKWH = float(input("Consumo de luz:"))
cliente = int(input("Cliente:"))
if cliente == 1:
    cons = qtdKWH*0.60
elif cliente == 2:
    cons = qtdKWH*0.48
elif cliente == 3:
    cons = qtdKWH*0.15
else:
    print("Cliente inválido:")
    cons = 0
print("KW/H =", cons)
'''

'''
#Programa: Produto desconto

produto = float(input("Preço do produto:"))
desc = 10
desConto = 8
if produto >= 1000:
    prom = produto * desc/100
elif produto <= 1000:
    prom = produto * desConto/100
elif produto < 0:
    prom = produto * 0
else:
    print("Preço inválido:")
    prom = 0
print(f"Promocão: R${prom} é o preço final de : R${produto - prom}")
'''

'''
#Programa salário

nome = input("Nome do funcionário:")
salario = float(input("Salário:"))
ts = int(input("Tempo de serviço:"))
if salario <=2000 and ts <=5:
    abono = 1000.00
elif salario <=2000 and ts >5:
    abono = 1500.00
elif ts <=8:
    abono = 1800.00
salarioTotal = salario + abono
print("Nome=", nome)
print("Salário total=", salarioTotal)
'''

#
horas = int(input("N de horas:"))
nivel = int(input("Nivel do professor:"))
if nivel ==1:
    sal = horas * 32.80
elif nivel ==2:
    sal = horas * 44.15
elif nivel ==3:
    sal = horas * 52.21
else:
    print("Nivel inválido")
    sal = 0
print("Salário = ", sal)























