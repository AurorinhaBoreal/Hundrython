# [Ex 40] Escreva um programa que retorne um número por extenso
from num2words import num2words # type: ignore

print("--------------------------------------------------------------------")
print("Escrita de números por extenso")
print("--------------------------------------------------------------------\n")

numero = int(input("Informe um número de 1 a 100:"))

numeroExtenso = num2words(numero, lang="pt_BR")

print(numeroExtenso)