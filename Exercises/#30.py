# [Ex 30] Calcule o preço de uma compra de combustivel

print("--------------------------------------------------------------------")
print("Postinho da Aurora 🪷")
print("--------------------------------------------------------------------\n")

combustivelArray = ["A - Álcool", "G - Gasolina"]
precoLitroArray = [2.70, 1.90]

print("|-------PRODUTOS-------|")
for i in range (len(combustivelArray)):
    print(f"{i+1} - {combustivelArray[i]} | R${precoLitroArray[i]:.3f}")
print("")

tipoCombustivel = str(input("Informe o tipo de combústivel desejado:"))
litroCombustivel = int(input("Informe quantos litros deseja abastecer:"))

if (tipoCombustivel == "A"):
    precoCombustivel = precoLitroArray[0]
    valorTotal = precoCombustivel*litroCombustivel

    if (litroCombustivel > 25):
        valorTotal = valorTotal*0.96
    else:
        valorTotal = valorTotal*0.98

    print(f"Comprando {litroCombustivel} litros de Álcool, o valor total é R${valorTotal:.2f}")
elif (tipoCombustivel == "B"):
    precoCombustivel = combustivelArray[1]
    valorTotal = precoCombustivel*litroCombustivel

    if (litroCombustivel > 25):
        valorTotal = valorTotal*0.95
    else:
        valorTotal = valorTotal*0.97
else:
    print("Informe um tipo de combustivel válido!")