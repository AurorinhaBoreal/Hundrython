print("--------------------------------------------------------------------")
print("Calculadora da nota Semestral de um Aluno")
print("--------------------------------------------------------------------\n")

print("--------------------------------------------------------------------")
print("Primeiro Bimestre")
print("--------------------------------------------------------------------\n")
b1prova1 = float(input("Qual a nota do aluno na 1° prova ? "))
b1prova2 = float(input("\nQual a nota do aluno na 2° prova ? "))

print("\n\n\n--------------------------------------------------------------------")
print("Segundo Bimestre")
print("--------------------------------------------------------------------\n")
b2prova1 = float(input("Qual a nota do aluno na 1° prova ? "))
b2prova2 = float(input("\nQual a nota do aluno na 2° prova ? "))

mediaBimeste1 = (b1prova1 + b1prova2) / 2
mediaBimeste2 = (b2prova1 + b2prova2) / 2
mediaFinal = (mediaBimeste1 + mediaBimeste2) / 2

print(f"\n\nA média final do aluno é {mediaFinal: .2f}")

