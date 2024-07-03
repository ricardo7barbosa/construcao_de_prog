'''
#Programa Venda

pc = float(input("Digite o preço de custo unitário:"))
pv = float(input("Digite o preço de venda unitário:"))
qe = float(input("Digite a quantidade em estoque:"))
lu = pv - pc
le = lu * qe
print("Lucro unitário:", lu)
print("Lucro de estoque:", le)

'''


'''
#Program tinta e pincel

tinta = float(input("Digite o preço da tinta:"))
cartao = 15
dinheiro = 20
cheque = 20
descCredito = tinta -(tinta * cartao /100)
descDinheiro = tinta -(tinta * dinheiro /100)
desCheque = tinta -(tinta * cheque /100)
print(f"O valor a ser pago no cartão de crédito é R$ {descCredito}, com desconto de : {cartao}%")
print(f"O valor a ser pago no dinheiro é R$ {descDinheiro}, com desconto de : {dinheiro}%")
print(f"O valor a ser pago no cheque é R$ {desCheque}, com desconto de : {cheque}%")

'''
#

valor1 = 10
valor2 = 8
conta  = 0
while conta <= 5:
      valor1 = valor2 + conta
      valor2 = valor1 + conta
      conta  = conta  + 2
print(valor1)
print(valor2)
