#[Ex 3] Calcular a Área e o Perímetro de uma circuferencia informando o Raio
import math

print("--------------------------------------------------------------------")
print("Calculadora de Área e Perímetro de uma circuferencia baseada no raio")
print("--------------------------------------------------------------------\n")

raio = float(input("Informe o raio de sua circuferência em cm: "))

#C=2⋅π⋅r
perimetro = math.pi * 2 * raio
#A=π⋅r2
area = math.pi * math.pow(raio, 2)

print(f"\nA Ára de sua circuferência é {area: .2f}cm e o perímetro é {perimetro: .2f}cm")
