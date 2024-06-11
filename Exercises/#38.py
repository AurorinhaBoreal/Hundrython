# [Ex 38] Faça um programa para identificar um ano bissexto

print("--------------------------------------------------------------------")
print("Verificação de Ano Bissexto")
print("--------------------------------------------------------------------\n")

ano = int(input("Informe o ano que deseja verificar:"))

if (ano % 4 == 0):
    div4 = 1
else:
    div4 = 0
if (ano % 100 == 0):
    div100 = 1
else:
    div100 = 0
if (ano % 400 == 0):
    div400 = 1
else:
    div400 = 0

if (div4 == 1 and div100 == 0):
    print(f"O ano {ano} é bissexto")
elif (div100 == 1 and div400 == 1):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto!")
