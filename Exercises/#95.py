print("--------------------------------------------------------------------")
print("Linear")
print("--------------------------------------------------------------------\n")

#Escrever um algoritmo e implementá-lo em linguagem C que linearize uma matriz de 6 
#por 6, colocando os valores contidos nela em um vetor de 36 elementos e mostrar o 
#conteúdo do vetor. 

matriz = []
for i in range(6):
    linha = []
    for y in range(6):
        d = int(input(f"Digite o número de indíce {y} da lista {i}: "))
        linha.append(d)
    matriz.append(linha)

vetor = []
for linha in matriz:
    for elemento in linha:
        vetor.append(elemento)

print(f"\nA matriz linearizada em um único vetor se dá por:\n{vetor}")