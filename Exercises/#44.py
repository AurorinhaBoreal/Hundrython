# [Ex 46] Um programa que calcule da divisão de A por B (Ambos devem ser inteiros e positivos)

print("--------------------------------------------------------------------")
print("Divisão Válida")
print("--------------------------------------------------------------------\n")

dividendo = int(input("Informe o número a ser dividido: "))
divisor = int(input("Informe o divisor: "))

if (dividendo > 0 and divisor > 0):
    resultado = dividendo/divisor
    print(f"O resultado do cálculo é {resultado}")
else:
    print("Informe números válidos")