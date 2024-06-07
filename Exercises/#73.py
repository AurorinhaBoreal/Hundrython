import statistics
#baixar essa dependencia

print("--------------------------------------------------------------------")
print("Estatistica")
print("--------------------------------------------------------------------\n")

#Escreva um programa em C que leia um array de 20 inteiros, calcule e imprima:
#a. A moda dos elementos no array (elemento mais freqüente).
#b. A mediana dos elementos no array (elemento central)
#c. A média

numbers = []
for i in range(1, 21):
    d = int(input(f"Digite o número de ordem {i}: "))
    numbers.append(d)

moda = statistics.mode(numbers)
mediana = statistics.median(numbers)
media = statistics.mean(numbers)

print(f"\nDos números indicados, é possível coletar os seguintes dados:\nModa: {moda}\nMediana: {mediana}\nMédia: {media}")