print("--------------------------------------------------------------------")
print("Amizade numeral")
print("--------------------------------------------------------------------\n")

#Dizemos que dois números são amigos se cada um deles é igual a soma dos divisores
#próprios do outro. Os divisores próprios de um número positivo N são todos os divisores
#inteiros positivos de N exceto o próprio N. Um exemplo de números amigos são 284 e
##220, pois os divisores próprios de 220 são 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 e 110.
#Efetuando a soma destes números obtemos o resultado 284 (1 + 2 + 4 + 5 + 10 + 11 + 20
#+ 22 + 44 + 55 + 110 = 284). Os divisores próprios de 284 são 1, 2, 4, 71 e 142,
#efetuando a soma destes números obtemos o resultado 220 (1 + 2 + 4 + 71 + 142 = 220).
#Escreva um programa que dado dois inteiros, verifique se eles são amigos. (17296 e
#18416 são amigos, por exemplo).

#Passos:
# Identificar todos os divisores de n1 e n2 - reciclar parte da função Primo da #49.py
# Realizar a soma dos divisores e comparar com n1 e n2
n1divisors = []
n2divisors = []

n1 = int(input("Insira o primeiro número: ")) 
n2 = int(input("Insira o segundo número: "))

soma1 = 0
soma2 = 0

i = 1
while i <= n1/2:
    if n1 % i == 0:
        n1divisors.append(i)
    i = i + 1

i = 1
while i <= n2/2:
    if n2 % i == 0:
        n2divisors.append(i)
    i = i + 1  

for numb in n1divisors:
    soma1 += numb
for numb in n2divisors:
    soma2 += numb

if soma1 == n2 and soma2 == n1:
    print("\nEsses dois números são amigos :D")
else:
    print("\nEsses dois números não são amigos :(")