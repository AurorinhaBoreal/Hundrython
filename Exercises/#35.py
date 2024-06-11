print("--------------------------------------------------------------------")
print("Programa que retorne um dia da semana")
print("--------------------------------------------------------------------\n")

#Usar dicionário novamente pq ajuda nessas situações
semana = [{1: 'Domingo'}, {2: 'Segunda'}, {3: 'Terça-Feira'}, {4:'Quarta-Feira'}, {5:'Quinta-Feira'}, {6:'Sexta-Feira'}, {7:'Sábado'}]

dia = int(input("Insira o dia da semana: "))

print(f"O dia da semana de número {dia} é {semana[dia-1].get(dia)}")

#Deu certo dnv poucas ideias