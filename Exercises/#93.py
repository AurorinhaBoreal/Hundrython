print("--------------------------------------------------------------------")
print("Matriz")
print("--------------------------------------------------------------------\n")

#Faça um programa em cobra para ler valores e armazená-los em uma matriz D 5 x 5. A seguir
#o programa deverá calcular a soma dos valores que compõem a diagonal principal e a
#diagonal secundária da matriz.
# 
#Queria ter prestado atenção nas aulas de matemáticas no Ensino médio....

matrizD = []
for i in range(1, 3):
    linha = []
    for y in range(1, 3):
        d = int(input(f"Digite o número de ordem {y} da lista {i}: "))
        linha.append(d)
    matrizD.append(linha)