#Programa Conta de luz2

qtd = float(input("Quantidade de Kwh:"))
cliente = int(input("Tipos de cliente:"))
if cliente == 1:
    conta = qtd * 0.60
elif cliente == 2:
    conta = qtd * 0.48
elif cliente == 3:
    conta = qtd * 0.15
else:
    print("Conta inválida")
    
print("Consumo da conta é:", conta)
