print("--------------------------------------------------------------------")
print("Digito verificadores")
print("--------------------------------------------------------------------\n")

#Digitos Verificadores são números especificos para identificar a validade de determinados usuários. 
#São utilizados em bancos, nesse cdaso são utilizados para verificar a agẽncia de uma conta:  
#É feita uma conta com os 4 primeiros digitos para identificar o último e dessa forma o número completo da agência da conta, 
#esse cálculo é chamado de módulo 11 Ex: 4870-X  
#Primeiramente, pegamos os números de menor valor para maior (da direita pra esquerda) e os organizamos: 
#Ex: 4870 -> 0784  Após isso, os multiplicamos por 2, 3, 4 e 5 e os somamos: (2x0) + (3x7) + (4x8) + (4x5) = 73  
#Dividimos o resultado por 11 e pegamos o resto da divisão (o cálculo de resto de divisão é chamado de módulo): 73 mod(11) = 7  
#Pegamos o resultado do módulo e subtraimos de 11 11 - 7 = 4  
#O resultado é o número completo da agência: Res: 4870-4  
#Faça um programa que receba os 4 primeiros números e informe o número completo.

card = input("Digite os quatro primeiros números para obter seu digito verificador: ")
cardlist = list(card)

numberReversed = ""
i = 0

if len(cardlist) == 4:
    for i in reversed(cardlist):
        numberReversed += i
else:
    print("\nNumero digitado não possui 4 digitos, tente novamente")
    exit()

verificador = 0
multiplier = 2
for digito in numberReversed:
    verificador += int(digito) * multiplier

    multiplier += 1

resto = verificador % 11
resto = 11 - resto
print('\n')
print(f"O seu digito verificador é {resto}\n\nSeu número é {card}-{resto}")
