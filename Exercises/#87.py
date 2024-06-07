print("--------------------------------------------------------------------")
print("Engual eu")
print("--------------------------------------------------------------------\n")

#Escreva um programa que verifique se duas strings são iguais, independente da
#caixa das letras. Por exemplo, este programa deve dizer que “Teste”é igual a “TeStE”.

str1 = input("Digite a primeira string: ")
str1 = str1.capitalize()
str2 = input("Digite a segunda string: ")
str2 = str2.capitalize()

if str1 == str2:
    print("\nAs strings são enguais")
else:
    print("\nElas não são enguais :(")
