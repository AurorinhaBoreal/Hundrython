print("--------------------------------------------------------------------")
print("Que vença o maior")
print("--------------------------------------------------------------------\n")

#Faça um programa em PYTHONNNNNNN que leia dois vetores de 10 posições de inteiros e copie o maior
#valor dos dois em cada posição em um terceiro vetor. Em seguida, imprima este terceiro
#vetor.

numbers1 = []
numbers2 = []
numbers3 = []

for i in range(1, 6):
    d = int(input(f"Digite o número de ordem {i} para o primeiro vetor: "))
    numbers1.append(d)

print("\nAgora o segundo vetor!\n")

for i in range(1, 6):
    d = int(input(f"Digite o número de ordem {i} para o segundo vetor: "))
    numbers2.append(d)

for i in numbers1:
    if numbers1[i] >= numbers2[i]:
        numbers3.append(numbers1[i])
    else:
        numbers3.append(numbers2[i])

print(f"O vetor novo é: ")
print(numbers3)



