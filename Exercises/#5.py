#[Ex 5] Ler um número inteiro e exibir o seu sucessor
import math

print("--------------------------------------------------------------------")
print("Sucessor do número que você digitou")
print("--------------------------------------------------------------------\n")

numero = float(input("Digite um número: "))

sucessor = math.floor(numero + 1)

print(f"\nO sucessor de seu número é {sucessor}")