# [Ex 26] Insira 3 números e receba a soma dos dois maiores entre eles

print("--------------------------------------------------------------------")
print("Soma dos Maiores Números")
print("--------------------------------------------------------------------\n")

numero1 = int(input("Informe o 1° número:"))
numero2 = int(input("Informe o 2° número:"))
numero3 = int(input("Informe o 3° número:"))

numeros = [numero1, numero2, numero3]

numeros.sort(reverse=True)

soma = numeros[0] + numeros[1]

print(f"Somando os maiors números do Array: {numeros[0]} e {numeros[1]}, nós temos como resultado {soma}")