#ProgramaVenda

pc = float(input("Digite o preço do custo unitário:"))
pv = float(input("Digite o preço de venda unitário:"))
qe = int(input("Digite a quantidade em estoque:"))
lu = pv - pc
le = lu * qe
print("Lucro unitário:", lu)
print("Lucro de estoque:", le)
