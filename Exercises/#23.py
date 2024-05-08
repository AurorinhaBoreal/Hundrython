#Escreva um programa que leia um número e imprima se este número é ou não par.
print("--------------------------------------------------------------------")
print("Algoritmo para verificar se é par ou ímpar")
print("--------------------------------------------------------------------\n")

n = int(input("Qual seu número? "))

resto = n % 2

if resto != 0:
    print("\nO seu número é ímpar")
else:
    print("\nO seu número é par")