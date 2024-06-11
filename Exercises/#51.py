print("--------------------------------------------------------------------")
print("Fibonacho")
print("--------------------------------------------------------------------\n")

#A série de Fibonacci é formada pela sequencia: 
#• 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
#Escreva um programa que gere a série de FIBONACCI até o N-ésimo termo (com N 
#sendo uma entrada do algoritmo).

#Fórmula do Brasil Escola "Fn=Fn−1+Fn−2,n≥3"

n = int(input("Digite o N-ésimo termo: "))

f1 = 1
f2 = 1
fn = 2

while fn < n:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    print(fn)
    