import math

print("--------------------------------------------------------------------")
print("Polares Opostos")
print("--------------------------------------------------------------------\n")

#Faça um programa em cobrinha que leia um array de 20 inteiros e imprima o menor e o maior
#valor dentre os elementos do array, bem como suas respectivas posições

#Aprendi coisas novas novamente, a função 'index' é muito útil

qnt = 0
numbers = []
for i in range(1, 21):
    d = int(input(f"Digite o número de ordem {i}: "))
    numbers.append(d)

min = min(numbers)
max = max(numbers)

print(f"\nO menor número digitado é {min}, na posição de index", numbers.index(min))
print(f"\nO maior número digitado é {max}, na posição de index", numbers.index(max))