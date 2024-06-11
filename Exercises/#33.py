print("--------------------------------------------------------------------")
print("Algoritmo que leia 2 valores e informe a qual quadrante o ponto pertence")
print("--------------------------------------------------------------------\n")

x = int(input("Insira o valor de X: "))
y = int(input("Insira o valor de Y: "))

if x > 0 and y > 0:
    print("O ponto está no 1º Quadrante, pois x e y são positivos")
elif x < 0 and y < 0:
    print("O ponto está no 3° Quadrante pois x e y são negativos")
elif x < 0 and y > 0:
    print("O ponto está no 2° Quadrante")
elif x > 0 and y < 0:
    print("O ponto está no 4° Quadrante")
elif x == 0 and y == 0:
    print("O ponto está na origem")
elif x == 0:
    print("O ponto está sob o eixo Y, vertical")
elif y == 0:
    print("O ponto está sob o eixo X, horizontal")




