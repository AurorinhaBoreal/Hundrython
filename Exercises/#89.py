print("--------------------------------------------------------------------")
print("Tratamento de string")
print("--------------------------------------------------------------------\n")

#Escreva um programa que gere uma string composta pelo último nome, seguido de
#virgula e as iniciais dos demais nomes (em ordem), seguida de ponto. Por exemplo, se a
#string entrada for “Gabriel Garcia Marquez”, a string gerada deve ser “Marquez, G. G.”

nome = input("Insira o seu nome composto: ")
resto = ''

nomeSeparados = nome.split(" ")
ultimo = nomeSeparados[len(nomeSeparados) - 1]
for i in range(0, len(nomeSeparados) - 1, 1):
    temp = nomeSeparados[i]
    if temp == temp.capitalize():
       resto += temp[0]
       resto += '. '

#Print final
print(f"\n{ultimo} {resto}")