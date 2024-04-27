print("--------------------------------------------------------------------")
print("Algoritmo para calcular a resistência equivalente")
print("--------------------------------------------------------------------\n")

r1 = float(input("O valor da primeira resistencia em Ohms em paralelo: "))
r2 = float(input("O valor da segunda resistencia em Ohms em paralelo: "))

r3 = float(input("\nAgora, o valor da ultima resistencia em sequencia: "))

# Req = (R1 . R2 / R1 + R2) + R3

rE = (r1 * r2) / (r1 + r2) + r3

print(f"\n A resistencia total do circuito é de {rE: .2f}") 