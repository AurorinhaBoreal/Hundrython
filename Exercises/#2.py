#[Ex 2] Calcular Área e Perímetro de um quadrado a partir de um lado

print("--------------------------------------------------------------------")
print("Área e Perimetro de um Quadrado")
print("--------------------------------------------------------------------\n")

lado = int(input("Informe a medida de um lado do quadrado em metros: "))

area = (lado*lado)
perimetro = (lado*4)
print(f"A área do quadrado é {area}m² e o perimetro é {perimetro} metros")