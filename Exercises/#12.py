# [Ex 12] COnverter uma velocidade de m/s para km/h ou vice-versa

print("--------------------------------------------------------------------")
print("Conversão de Velocidades")
print("--------------------------------------------------------------------\n")

print("Informe o tipo de conversão que deseja fazer:")
print("1-Converter m/s para km/h")
print("2-Converter km/h para m/s")
conversao = int(input("Selecione digitando o número:"))

if (conversao == 1):
    velocidade = float(input("Informe a velocidade para conversão:"))

    velConvertida = velocidade * 3.6

    print(f"A velocidade {velocidade}m/s convertida para km/h é {velConvertida}km/h")
elif (conversao == 2):
    velocidade = float(input("Informe a velocidade para conversão:"))

    velConvertida = velocidade / 3.6

    print(f"A velocidade {velocidade}km/h convertida para m/s é {velConvertida}m/s")
else:
    print("Informe um número válido!")
