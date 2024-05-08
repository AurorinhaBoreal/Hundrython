print("--------------------------------------------------------------------")
print("Algoritmo para calcular a altura do prédio")
print("--------------------------------------------------------------------\n")

pessoaAltura = float(input("Informe a sua altura em cm: "))
sombraPessoaAltura = float(input("Informe a altura de sua sombra em cm: "))
sombraPredioAltura = float(input("Informe a altura da sombra do prédio em metros: "))

#Conversão para cm
sombraPredioAltura = sombraPredioAltura * 100

# Explicação: Se coloque ao lado deste edifício. O edifício projeta uma sombra no chão que você precisa saber quanto mede. Você projeta uma sobra no chão, meça-a também. 
# Suponha que você conhece a sua altura (neste caso 2 m), então isto basta para aplicar o Teorema de Tales que nada mais é do que comparar a sua altura com a altura do 
# prédio através da sombra que vocês projetam.

#Aplicando o Teorema de Tales: H/h = S/s, sendo h-H as alturas pequenas e grandes e s-S as sombras pequenas e grandes.
alturaPredio = (sombraPredioAltura / sombraPessoaAltura) * pessoaAltura

print(f"De acordo com os dados apresentados, a altura do prédio é de {alturaPredio: .2f}cm, ou {alturaPredio / 100: .2f}m")