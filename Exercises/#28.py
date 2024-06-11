# [Ex 28] Insira 3 números e receba a soma dos dois maiores entre eles

print("--------------------------------------------------------------------")
print("Verificação de Letra")
print("--------------------------------------------------------------------\n")

vogais = ["a", "e", "i", "o", "u"]

letra = str(input("Insira uma letra:"))

# PODIA RETORNAR -1 IGUAL TODA OUTRA LINGUAGEM, MAS NÃÃÃÃÃOOOOOO...
try:
    vogais = vogais.index(letra)
    print(f"A letra \"{letra}\" é uma vogal.")
except ValueError:
    print(f"A letra \"{letra}\" é uma consoante.")
