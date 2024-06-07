# [Ex 20] Faça um sistema de vendas de uma loja

print("--------------------------------------------------------------------")
print("Lojinha da Aurora 🌸")
print("--------------------------------------------------------------------\n")

nomeProdutosArray = ["Perfume Chique", "Televisão 120 Polegadas", "PlayStatoin VII", "The First Of Us III - PSVIII"]
precoProdutosArray = [400.00, 7000.00, 5000.00, 400.00]

print("|-------PRODUTOS-------|")
for i in range (len(nomeProdutosArray)):
    print(f"{i+1} - {nomeProdutosArray[i]} | R${precoProdutosArray[i]}")
print("")

produto = int(input("Digite o número do produto desejado:"))-1
entrada = float(input("Informe o valor de entrada que deseja pagar:"))
restante = precoProdutosArray[produto] - entrada

if (entrada < restante/2):
    print("O valor de entrada deve ser maior que o valor de cada parcela")
else:
    parcela = restante/2

    print(f"Para pagar o {nomeProdutosArray[produto]} foi dado de entrada R${entrada:.2f} e posteriormente serão pagas duas parcelas de R${parcela}")