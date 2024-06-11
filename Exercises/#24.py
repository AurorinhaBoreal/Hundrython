# [Ex 24] Insira 3 números e mostre o maior


print("--------------------------------------------------------------------")
print("Identificador do Maior Número")
print("--------------------------------------------------------------------\n")

numero1 = int(input("Informe o 1° número:"))
numero2 = int(input("Informe o 2° número:"))
numero3 = int(input("Informe o 3° número:"))

numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)

print(f"O maior número entre os três é {numeros[0]}")