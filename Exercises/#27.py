print("--------------------------------------------------------------------")
print("Insira 3 números e receba a média ponderada deless")
print("--------------------------------------------------------------------\n")
#Para o calculo da média ponderada = O maior valor tem peso 5, Os outros 2 tem peso 2.5

valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))
valor3 = float(input("Insira o terceiro valor: "))

peso1 = 5
peso2 = 2.5

if valor1 > valor2 and valor1 > valor3:
    valor1 = valor1 * 5
    valor2 = valor2 * 2.5
    valor3 = valor3 * 2.5
elif valor2 > valor3 and valor2 > valor1:
    valor1 = valor1 * 2.5
    valor2 = valor2 * 5
    valor3 = valor3 * 2.5
elif valor3 > valor2 and valor3 > valor1:
    valor1 = valor1 * 2.5
    valor2 = valor2 * 2.5
    valor3 = valor3 * 5

pandero = (valor1 + valor2 + valor3) / (peso1 + (peso2*2))

print(f"A média ponderada dos respectivos valores, considerando os pesos já atribuídos, a média ponderada dos valores é de {pandero}")