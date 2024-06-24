#Estrutura de Decisão Múltipla

#Nível          Valor da hora/aula
#   1           32.80
#   2           44.15
#   3           52.21


horas = int(input("N de horas:"))
nivel = int(input("Nível de professor:"))
if nivel == 1:
    sal = horas * 32.80
elif nivel == 2:
    sal = horas * 44.15
elif nivel == 3:
    sal = horas * 52.21
else:
    print("Nível Inválido")
    sal = 0
print("Salário =:", sal)
