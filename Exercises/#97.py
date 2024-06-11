print("--------------------------------------------------------------------")
print("Linear")
print("--------------------------------------------------------------------\n")

#Escrever um algoritmo e implementá-lo em linguagem COBRA que leia uma matriz de valores 
#inteiros 5 por 5 e a exiba. A seguir,  leia dois números x e y e em seguida troque a x
#ésima linha pela y-ésima linha, a x-ésima coluna com a y-ésima coluna, a diagonal 
#principal com a secundária e, por fim mostre a matriz assim modificada. 

matriz = []
for i in range(5):
    linha = []
    for y in range(5):
        d = int(input(f"Digite o número de indíce {y} da lista {i}: "))
        linha.append(d)
    matriz.append(linha)
 
def exibir(matriz):
    for linha in matriz:
        print(' '.join(map(str, linha)))

print(f"A matriz inserida se dá por: {exibir(matriz)}")

x = int(input("\nDigite o índice da linha e coluna x (0 a 4): "))
y = int(input("Digite o índice da linha e coluna y (0 a 4): "))


#Troca das linhas
for i in range(5):
    matriz[x], matriz[y] = matriz[y], matriz[x]

#Troca das colunas
for i in range(5):
    matriz[i][x], matriz[i][y] = matriz[i][y], matriz[i][x]

#Troca das diagonais
for i in range(5):
    matriz[i][i], matriz[i][4-i] = matriz[i][4-i], matriz[i][i]

print(f"A matriz Nova se dá por: {exibir(matriz)}")
