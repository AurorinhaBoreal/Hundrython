#[Ex 6] Ler dois números inteiros, exibir o quociente e o resto da divisão entre eles
import math;

print("--------------------------------------------------------------------")
print("Quociente e Resto de Divisão de dois Números")
print("--------------------------------------------------------------------\n")

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

quociente = int(num1 / num2)

resto = num1 % num2

print(f"O quociente de divisão é {quociente}, já o resto é {resto}")