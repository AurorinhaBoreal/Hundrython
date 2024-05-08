#[Ex 1] Calcular Área e Perímetro de um retângulo informando a Base e Altura
print("-------------------------------------------------------")
print("Calculadora de Área e Perímetro baseado na Base e Altura")
print("-------------------------------------------------------\n")

base = int(input("Qual a base de seu retângulo em cm? "))

altura = int(input("Qual a altura de seu retângulo em cm? "))

area = base * altura
perimetro = (base * 2) + (altura * 2)

print(f"\nA Área de seu retângulo é {area}cm e o perímetro é igual a {perimetro}cm")


