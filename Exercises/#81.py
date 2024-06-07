print("--------------------------------------------------------------------")
print("Whitespaces")
print("--------------------------------------------------------------------\n")

#Escreva um programa em python que normalize uma string lida, em uma nova string.
#Normalizar uma string é o processo de remover os espaços excedentes que separam as
#palavras

string1 = input("Digite uma string: ")
string1 = string1.replace(" ", "")

print(f"\n{string1}")