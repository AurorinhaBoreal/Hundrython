print("--------------------------------------------------------------------")
print("População e ultrapassagem omg")
print("--------------------------------------------------------------------\n")

#Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e
#um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escreva
#um programa, que imprima o tempo necessário para que a população do país A ultrapasse
#a população do país B.

a = 5000000
b = 7000000

input("\nA quantidade de população é fixa, então você não tem input dessa vez, mas aperta algo ai\n")

anos = 0

while a <= b:
    anos += 1
    a += (a/100) * 3
    b += (b/100) * 2
    print(f"\nAno: {anos}\n{a: .0f}\n{b: .0f}")
    
print(f"\nLevou {anos} anos\n")
    

