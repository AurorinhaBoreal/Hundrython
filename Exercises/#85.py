import math

print("--------------------------------------------------------------------")
print("Conversão de bases")
print("--------------------------------------------------------------------\n")

#Escreva um programa que leia uma string representando um número hexadecimal (base 16) 
#e imprima sua representação em decimal (base 10).

hexd = input("Digite um número Hexadecimal: ")

dec = sum(int(x, 16) * math.pow(16, len(hexd)-i-1) for i, x in enumerate(hexd))

print(f"\nO seu número em decimal é {dec}")