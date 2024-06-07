print("--------------------------------------------------------------------")
print("Bubble try")
print("--------------------------------------------------------------------\n")

#Escreva um programa que ordene um array de inteiros de 15 posições utilizando o
#método da bolha (bubble sort).

#Explicação
#Bubble Sort é um algoritmo de classificação comumente usado em ciência da computação. O Bubble Sort baseia-se na ideia de comparar repetidamente pares de elementos adjacentes e, em seguida, trocar as suas posições se existirem na ordem errada.
#
#Algoritmo de classificação de bolhas: 
#
#Em uma matriz(APLICAVEL PARA LISTAS) não classificada de 5 elementos, comece com os dois primeiros elementos e classifique-os em ordem crescente. 
#(Compare oS elementos para verificar qual é o maior).
#Compare o segundo e o terceiro elemento para verificar qual é o maior e classifique-os em ordem crescente.
#Compare o terceiro e o quarto elemento para verificar qual é o maior e classifique-os em ordem crescente.
#Compare o quarto e o quinto elemento para verificar qual é o maior e classifique-os em ordem crescente.
#Repita as etapas 1–5 até que não sejam necessárias mais trocas.

numbers = []
for i in range(1, 6):
    d = int(input(f"Digite o número de ordem {i}: "))
    numbers.append(d)

#Não será utilizado bibliotecas, irei criar uma classe para o sort

def bSort1(x):
    index = 0
    for j in range(len(x) - 1, 1):
        if x[index] < x[index+1]:
            x[index] = x[index]
        elif x[index] > x[index+1]:
            x[index] = x[index+1]
        else:
            x[index] = j
        index += 1
    return x

def bSort2(x):
    for i in range(0,len(x)-1), 1: 
        for j in range(len(x)-1, 1): 
            if(x[j]>x[j+1]):  
                x[j] = x[j+1] 
                x[j+1] = x[j] 
    return x 

def bSort3(x):
    for i in range(0, len(x) -1, 1):
        for j in range(len(x) -1, 1):
            if x[j] > x[j+1]:
                y = x[j]
                x[j] = x[j+1]
                x[j+1] = y
    return x

res = bSort3(numbers)
print(f"\n{res}")

