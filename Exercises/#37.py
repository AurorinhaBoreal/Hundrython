print("Exterminação de pragas 2000")

print('\n\n1 - Ervas Daninhas | R$50,00/Acre')
print('2 - Gafanhotos | R$100,00/Acre')
print('3 - Broca | R$150,00/Acre')
print('4 - Todos Acima | R$250,00/Acre')


praga = int(input("\nQual das Opções acima sua infestação se encaixa? "))

print('\nDescontos:')
print('Área superior a 1000 Acres: 5%')
print('Custo maior que R$750,00: 10 por cento ao valor que ultrapassar')

area = float(input("\nLevando em conta os descontos apresentados, qual é a area da infestação em acres? "))
valor = 0

if praga == 1:
    valor = area * 50
elif praga == 2:
    valor = area * 100
elif praga == 3:
    valor = area * 150
elif praga == 4:
    valor = area * 250

if area > 1000:
    valor = valor * 0.95

if valor > 750:
    valor = valor * 0.90

print(f"\nA sua area em acres de {area}, resulta em um valor de {valor} após descontos")