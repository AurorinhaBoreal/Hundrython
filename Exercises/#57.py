import math

print("--------------------------------------------------------------------")
print("Mais números")
print("--------------------------------------------------------------------\n")

#Sendo S = 1 + 1/(2^2) + 1/(3^3) + 1/(4^4) + 1/(5^5).... + 1/(N^N)
#Escreva um programa que calcule S para um número N digitado pelo usuário

#Essa foi mais simples do que pensei
print("Sendo S = 1 + 1/(2^2) + 1/(3^3) + 1/(4^4) + 1/(5^5).... + 1/(N^N)")
n = int(input("Insira um número N para obter seu S: "))

res = 1
i = 1
while i <= n:
    res += 1/(math.pow(i, i))
    i += 1

print("\n")
print(f"O seu número é {res: .2f}")
