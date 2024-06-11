# [Ex 22] Insira um número e mostre seu módulo

print("--------------------------------------------------------------------")
print("Valor do Módulo")
print("--------------------------------------------------------------------\n")

numero = int(input("Informe um número para ser buscado o modulo do mesmo:"))

if (numero < 0):
    modulo = -numero

print(f"O número informado foi {numero}, o módulo desse número é |{modulo}|")
