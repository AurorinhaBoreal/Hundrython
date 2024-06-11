print("--------------------------------------------------------------------")
print("Algoritmo para calcular a raiz de uma função do primeiro grau")
print("--------------------------------------------------------------------\n")
#Raiz de uma função (seja qual for o grau) é todo número que, ao ser substituído na equação (no lugar de “x”), tem a capacidade de zerar a sentença

#Isso daqui é uma função do 1° grau: f(x) = ax + b, ou isso y = 3x + b
#O usuário então deve digitar (A) e (B)

print("Considere sua equação do primeiro grau neste formato: y = ax + b")
a = int(input("Qual o valor de A na sua equação? "))
b = int(input("Qual o valor de B na sua equação? "))

x = -b/a

print(f"\nSua raiz é de {x}")

