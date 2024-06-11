# [Ex 18] Escreva um programa que troque o valor de duas variaveis

print("--------------------------------------------------------------------")
print("Inverter a Formatação de um número")
print("--------------------------------------------------------------------\n")


variavelA = int(input("Informe um valor para a variavel A:"))
variavelB = int(input("Informe um valor para a variavel B:"))

print(f"Antes da Inversão: A: {variavelA} | B: {variavelB}")

variavelA = variavelA + variavelB
variavelB = variavelB - variavelA
variavelB = -variavelB
variavelA = variavelA - variavelB

print(f"Depois da Conversão: A: {variavelA} | B: {variavelB}")