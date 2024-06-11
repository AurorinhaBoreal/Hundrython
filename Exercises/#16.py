# [Ex 16] Formatar um número ao contrário

import math;

print("--------------------------------------------------------------------")
print("Inverter a Formatação de um número")
print("--------------------------------------------------------------------\n")


numero = str(input("Informe um número para ser invertido:"))

ReverseNumber = numero[::-1]

print(f"Numero Original: {numero} -> Número Invertido: {ReverseNumber}")