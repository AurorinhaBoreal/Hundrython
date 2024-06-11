print("--------------------------------------------------------------------")
print("Diagonaix")
print("--------------------------------------------------------------------\n")

#Faça um programa em cobra para ler valores e armazená-los em uma matriz D 5 x 5. A seguir
#o programa deverá calcular a soma dos valores que compõem a diagonal principal e a
#diagonal secundária da matriz.
# 
#Queria ter prestado atenção nas aulas de matemáticas no Ensino médio....

matrizD = []
for i in range(5):
    linha = []
    for y in range(5):
        d = int(input(f"Digite o número de indíce {y} da lista {i}: "))
        linha.append(d)
    matrizD.append(linha)

def Principal(matriz):
    soma = 0
    for i in range(5):
        soma += matriz[i][i]
    return soma

def Secuandaria(matriz):
    soma = 0
    for i in range(5):
        soma += matriz[i][4 - i]
    return soma

prin = Principal(matrizD)
sec = Secuandaria(matrizD)

print(f"\nA soma da diagonal principal é: {prin}")
print(f"\nA soma da diagonal secundária é: {sec}")