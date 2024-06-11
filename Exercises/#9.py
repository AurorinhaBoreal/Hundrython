import math
print("--------------------------------------------------------------------")
print("Dado o raio e a altura de um cilindro, calcular seu volume")
print("--------------------------------------------------------------------\n")

#O volume do cilindro de altura h e raio da base r é dado por: V=π⋅r2⋅h.

raio = float(input("\nInforme o raio do cilindro em cm: "))
altura = float(input("\nInforme a altura do cilindro em cm: "))

volume = (math.pi * (math.pow(raio, 2))) * altura

print(f"\nO volume do seu cilindro é {volume: .2f}cm")