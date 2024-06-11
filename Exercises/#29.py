print("--------------------------------------------------------------------")
print("Escreva um programa que calcule o desconto previdenciário de um funcionário")
print("--------------------------------------------------------------------\n")

#11% ou 334.29, o que for menor.

bruto = float(input("Digite o seu sálario bruto: "))
desc = 0

if (11/100 * bruto) >= 334.29:
    desc = 334.29
else:
    desc = (11/100 * bruto)
    
print(f"O desconto previdenciário é de R${desc: .2f}, sendo o salário pós desconto R${bruto-desc: .2f}")