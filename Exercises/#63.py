print("--------------------------------------------------------------------")
print("Quantas são pares ??")
print("--------------------------------------------------------------------\n")

#Faça um programa em pitu que leia um array de 10 posições e conte quantos números pares
#são elementos do array. Imprima esta quantidade.

qnt = 0
numbers = []
for i in range(1, 11):
    d = int(input(f"Digite o número de ordem {i}: "))
    numbers.append(d)

for i in numbers:
    if i % 2 == 0:
        qnt += 1

print(f"\nDos 10 números digitados, foram identificados {qnt} números pares")