import numpy

print("--------------------------------------------------------------------")
print("Matriz")
print("--------------------------------------------------------------------\n")

#Elabore um programa em que leia valores inteiros para preencher uma matriz A 5 x 5.
#Você deverá criar adicionalmente dois vetores de 5 elementos: somaLinhas e
#somaColunas. Em cada posição do vetor somaLinhas deverá ser armazenada a soma da
#linha correspondente na matriz A. Da mesma forma, em cada posição do vetor
#somaColunas deverá ser armazenada a soma da coluna correspondente na matriz A.

matriz1 = []
for i in range(1, 6):
    linha = []
    for y in range(1, 6):
        d = int(input(f"Digite o número de ordem {y} da lista {i}: "))
        linha.append(d)
    matriz1.append(linha)

print(matriz1)

def Calc(matriz):
    tamanho = len(matriz)
    somaLinhas = [0] * tamanho
    somaColunas = [0] * tamanho

    for i in range(tamanho):
        for j in range(tamanho):
            somaLinhas[i] += matriz[i][j]
            somaColunas[j] += matriz[i][j]
    
    return somaLinhas, somaColunas

somaLinhas, somaColunas = Calc(matriz1)

print(f"\nA soma das linhas é :{somaLinhas}")
print(f"\nA soma das colunas é: {somaColunas}\n")