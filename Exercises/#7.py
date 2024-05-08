#Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, meses e dias.
import math
print("--------------------------------------------------------------------")
print("Contador de Idade")
print("--------------------------------------------------------------------\n")

diasTotal = int(input("Quantos dias você tem? "))

anos = math.floor(diasTotal / 365.25)
meses = math.floor((diasTotal % 365.25) / 30)
dias = math.floor((diasTotal % 365.25) % 30)

print(f"\nCom base nos seus dias vividos, você tem {anos} anos, {meses} meses e {dias} dias de vida!\n")


