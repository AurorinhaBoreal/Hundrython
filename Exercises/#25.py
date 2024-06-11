print("--------------------------------------------------------------------")
print("Algoritmo para saber os dias do mês")
print("--------------------------------------------------------------------\n")

#Utilizar dicionário aqui pra dar uma brincada
meses = [{'Janeiro': 1, 'Dias':31}, {'Fevereiro': 2, 'Dias': '28 ou 29 se o ano for bisexto'}, {'Março': 3, 'Dias':31}, {'Abril': 4,'Dias':30}, {'Maio': 5, 'Dias':31}, {'Junho': 6,'Dias':30}, {'Julho':7,'Dias':31}, {'Agosto': 8,'Dias':31}, {'Setembro':9, 'Dias':30}, {'Outubro': 10, 'Dias':31}, {'Novembro': 11, 'Dias':30}, {'Dezembro': 12, 'Dias':31}]

print(f"\n1 - Janeiro\n2 - Fevereiro \n3 - Março\n4 - Abril\n5 - Maio\n6 - Junho\n7 - Julho\n8 - Agosto\n9 - Setembro\n10 - Outubro\n11 - Novembro\n12 - Dezembro")

mesEscolhido = int(input("Consulte a tabela acima e digite o numero do mês que deseja consultar o dia: "))

print(f"Nesse mês, Há {meses[mesEscolhido -1].get('Dias')} dias")