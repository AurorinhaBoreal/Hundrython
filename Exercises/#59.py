import math

print("--------------------------------------------------------------------")
print("Número de Euler")
print("--------------------------------------------------------------------\n")

#O número 'e' (número de Euler) pode ser representado e calculado por meio da utilização
#da série de Taylor para e quando x=1, como a soma da seguinte série infinita:
#
# e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
# 
#Escreva um programa, que leia o número de termos da série (n) e imprima como saída, o
#cálculo do número de Euler para cada um dos n primeiros elementos da série.

e = 1
res = 0
n = int(input("Digite o número de termos da sua série de Taylor para receber um Número de Euler 'e': "))
i = 1

while i < n:
    e += i/(math.factorial(i))
    i += 1

print(f"\nO seu número de eule segundo a série de taylor é: {e: .2f}")