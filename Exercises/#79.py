print("--------------------------------------------------------------------")
print("Substring")
print("--------------------------------------------------------------------\n")

#Escreva um programa em p, que gere a substring de uma string original, dado a posição
#inicial e a final da substring.

res = "Essa é a string original, você irá retirar uma substring dela!"
print(f"{res}\n")

n1 = int(input("Posição Inicial da substring: "))
n2 = int(input("Posição Final da substring: "))

if n1 > len(res) or n2 > len(res):
    print(f"\nA posição inserida ultrapassa o tamanho da string\n")
else:
    pi = res[n1:n2]
    print(f"\n{pi}\n")

