import math

print("--------------------------------------------------------------------")
print("Número X é primo??")
print("--------------------------------------------------------------------\n")

def Primo(x):
    i = 2
    while i <= math.sqrt(x):
        if x % i < 1:
            return False
        i += 1
    return x > 1
#Essa função foi bolada fala tu

x = int(input("Digite o número que achas que é primo: "))

primo = Primo(x)

if primo == True:
    print("\nO número inserido é primo\n")
else:
    print("\nO número inserido não é primo\n'")