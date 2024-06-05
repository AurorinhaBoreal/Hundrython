print("--------------------------------------------------------------------")
print("Aonde aparece primeiro?")
print("--------------------------------------------------------------------\n")

#Escreva um programa que leia um vetor de 10 posições de inteiros e um inteiro. O
#programa deve informar a primeira posição onde este inteiro ocorre no vetor ou -1 caso o
#valor não ocorra no vetor (Busca Sequencial).

numbers = []
for i in range(1, 11):
    d = int(input(f"Digite o número de ordem {i}: "))
    numbers.append(d)
num = int(input("\nAgora informe um único número: "))

def buscaSequencial(numbers, num):
    for i in range(len(numbers)):
        if numbers[i] == num:
            return i
    return -1

res = buscaSequencial(numbers, num)

if res == -1:
    print(f"{res}, O número não está na lista")
else:
    print(f"\nO número está na ordem {res + 1}")