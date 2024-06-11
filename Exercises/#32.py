# [Ex 32] Leia um caractere e informe o seu tipo (consoante, vogal, número ou símbolo)

print("--------------------------------------------------------------------")
print("Verificação de Letras e Números")
print("--------------------------------------------------------------------\n")

caractere = str(input("Informe um caractere"))

vogais = "aeiou"

consoantes = "bcdfghjklmnopqrstvwxyz"

simbolos = "`-=~!@#$%^&*()_+[]{}|;:,.<>/?\\"

indexV = vogais.find(caractere)
indexC = consoantes.find(caractere)
indexS = simbolos.find(caractere)

if (indexS != -1):
    print("O caractere é um simbolo")
elif (indexV != -1 and indexC == -1):
    print("O caractere é uma vogal")
elif (indexC != -1 and indexV == -1):
    print("O caractere é uma consoante")
else:
    print("O caractere é um numero")



