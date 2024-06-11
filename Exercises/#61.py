print("--------------------------------------------------------------------")
print("Vetor 0")
print("--------------------------------------------------------------------\n")
#Faça um programa em python que crie e inicialize um array de 20 posições de inteiros com 0
#para cada elemento. Imprima o vetor em seguida, indicando a posição e o valor na
#posição (um por linha).

vetor = []
for i in range(0, 20, 1):
    vetor.append(0)

c = 1
for i in vetor:
    print(f"{c}° Posição - {vetor[i]}")
    c += 1