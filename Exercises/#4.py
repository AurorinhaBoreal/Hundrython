#[Ex 4] Dado três lados de um triângulo, informar seu perimetro

print("--------------------------------------------------------------------")
print("Perimetro de um Triângulo")
print("--------------------------------------------------------------------\n")

lado1 = int(input("Informe o 1° lado do triângulo: "))
lado2 = int(input("Informe o 2° lado do triângulo: "))
lado3 = int(input("Informe o 3° lado do triângulo: "))

perimetro = lado1+lado2+lado3

print(f"O perimetro do triângulo é {perimetro} metros")