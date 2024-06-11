#[Ex 8] Leia um valor de farenheit e mostre o em Celsius

print("--------------------------------------------------------------------")
print("Conversão de Farenheit para Celsius")
print("--------------------------------------------------------------------\n")

tempFarenheit = float(input("Informe a temperatura em Farenheit: "))

tempCelsius = (tempFarenheit - 32)*5/9

print(f"O equivalente de {tempFarenheit}°F em Celsius é {tempCelsius:,.2f}°C")