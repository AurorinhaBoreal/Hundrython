print("--------------------------------------------------------------------")
print("Repetições")
print("--------------------------------------------------------------------\n")

#Escreva um programa que leia um vetor de 15 posições de inteiros. Em seguida, o
#programa deve ler um valor inteiro e imprimir o número de vezes que este valor ocorre
#no vetor.

numbers = []
for i in range(1, 16):
    d = int(input(f"Digite o número de ordem {i}: "))
    numbers.append(d)

valor = int(input("Insira um número para comparação: "))
qnt = numbers.count(valor)

print(f"\nEsse valor aparece no vetor {qnt} vezes")