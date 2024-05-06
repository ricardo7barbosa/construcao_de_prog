#Programa Conta de luz

qtd = float(input("Quantidade de Kwh:"))
cliente = int(input("Tipos de cliente:"))
if cliente == 1:
    conta = qtd * 0.60
if cliente == 2:
    conta = qtd * 0.48
if cliente == 3:
    conta = qtd * 0.15
print("Consumo é:", conta)


