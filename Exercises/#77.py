print("--------------------------------------------------------------------")
print("Australia")
print("--------------------------------------------------------------------\n")

#Escreva um programa em pitu, que leia uma string, gere uma nova string com o texto
#invertido e imprima esta nova string

string1 = input("Digite uma string: ")
res = ''
for i in reversed(string1):
    res += i

print(f"\n{res}")

