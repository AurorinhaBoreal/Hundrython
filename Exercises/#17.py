print("--------------------------------------------------------------------")
print("Algoritmo para liberar dinheiro em cédula de saque de forma otimizada")
print("--------------------------------------------------------------------\n")

#Saques em caixas eletronicos não incluem centavos então INT
valorTotal = int(input("Qual o valor que deseja retirar? "))

ced1 = 0
ced2 = 0
ced5 = 0
ced10 = 0
ced20 = 0
ced50 = 0
ced100 = 0

while valorTotal >= 100:
    ced100 = ced100 + 1
    valorTotal = valorTotal - 100
while valorTotal >= 50:
    ced50 = ced50 + 1
    valorTotal = valorTotal - 50
while valorTotal >= 20:
    ced20 = ced20 + 1
    valorTotal = valorTotal - 20
while valorTotal >= 10:
    ced10 = ced10 + 1
    valorTotal = valorTotal - 10
while valorTotal >= 5:
    ced5 = ced5 + 1
    valorTotal = valorTotal - 5
while valorTotal >= 2:
    ced2 = ced2 + 1
    valorTotal = valorTotal - 2
while valorTotal >= 1:
    ced1 = ced1 + 1
    valorTotal = valorTotal - 1

print(f"Efetue o saque da seguinte forma: \n{ced100} notas de R$100\n{ced50} notas de R$50\n{ced20} notas de R$20\n{ced10} notas de R$10\n{ced5} notas de R$5\n{ced2} notas de R$2\n{ced1} notas de R$1")

