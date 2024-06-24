'''
#Programa de conversão

valorDolares = float(input("Digite o valor em dólares:"))
cotacao = float(input("Digite a cotação do dólar:"))
valorReais = valorDolares * cotacao
print("O valor em Reais:", valorReais)

'''
'''

#Programa print

funcionario = "João"
profissao = "Analista de Sistemas"
salario = 15000
print(funcionario, "é", profissao, "e ganha", salario)
print("A gratificação do",funcionario, "é", salario * (15/100))

'''
'''
#
A = 8
B = 18
AUX = A + B
A = AUX - A
B = AUX - B
print("Valor de A=", A)
print("Vaor de B=", B)

'''
#
a = int(input("Digite o valor:"))
b = int(input("Digite o valor:"))
c = int(input("Digite o valor:"))
d = (a+b)%c
print(d)
