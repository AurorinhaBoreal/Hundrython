#[ Ex 44] Imprima todos os números de 1 a 100 e a soma deles

print("--------------------------------------------------------------------")
print("Impressão e Soma de números!")
print("--------------------------------------------------------------------\n")

soma = 0

for i in range(101):
    soma += i
    print(i)

print(f"A soma dos 100 números é {soma}")