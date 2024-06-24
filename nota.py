'''
#Programa de treinamento if, elif, else

nota = float(input("Digite a nota:"))
if nota >= 9:
    print("Ótimo!")
elif nota >=8:
    print("Bom!")
elif nota >=7:
    print("Regular!")
else:
    print("Reprovado!")

'''

'''
#Programa porcentagem
valor = float(input("Digite o valor:"))
desconto = float(input("Digite o valor:"))
preco = valor * (desconto / 100)
print("O valor a ser pago é:", preco)

'''

#Programa de reajuste de sálario

salatual = float(input("Digite o valor do salário:"))
perc = float(input("O aumento:"))
reaj = salatual * (perc/100)
salafinal = salatual + reaj
print("O valor do salário com reajuste é:", salafinal)
