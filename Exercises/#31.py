print("--------------------------------------------------------------------")
print("Escreva um programa que calcule o Quaterback Rating")
print("--------------------------------------------------------------------\n")
#Para calcular o quarterback rating:
#Calcula o percentual de passes completados em relação aos passes tentados. Desse valor subtrai 0.3, após o divide por 0.2.@
#Calcula o valor de jardas passadas (No campo do jogo tem uns número, acho que é isso) em relação a quantidade de passes tentados, Deste valor, se subtrai 3, após o divide por 4.@
#Calcula-se a razão de passes para touchdowns em relação aos passes tentados e divide esse valor 0,05
#Por fim calcula-se a razão de passes interceptados sobre os passes tentados, deste valor se subtrai 0.095 e divide o resultado por 0.04.
#Por final, pegue esses 4 dados e some todos eles, após isso multiplique por 100 e por fim divida por 6.
#Fim.
#O limite de todos esses valores são Limite Sup: 2.375 | Limite Inf. 0. Caso passe, o valor fica limitado ao valor limite.

def limite(valor):
    if valor >= 2.395:
        valor = 2.395
        return valor
    elif valor <= 0:
        valor = 0
        return valor
    else:
        valor = valor
        return valor

passesTentativas = int(input("Tentativas Totais de Passes: "))
passesCompletos = int(input("Tentativas Sucessidades de Passes: "))

jardasPassadas = int(input("Jardas Atravessadas: "))
passesInterceptados = int(input("Passes Intercepctados: "))
touchDowns = int(input("Touchdowns: "))

passesFinal = ((passesTentativas - passesCompletos) / passesTentativas) * 100
passesFinal = (100 - passesFinal) - 0.3
passesFinal = passesFinal / 0.2
passesFinal = limite(passesFinal)

jardasFinal = ((jardasPassadas - passesTentativas)-3) / 4
jardasFinal = limite(jardasFinal)

touchDownsFinal = ((touchDowns / passesTentativas) - 3) / 4
touchDownsFinal = limite(touchDownsFinal)

interceptadosFinal = ((passesInterceptados / passesTentativas) - 0.095) / 0.04
interceptadosFinal = limite(interceptadosFinal)

qtRating = ((passesFinal + jardasFinal + touchDownsFinal + interceptadosFinal) * 100) / 6

print(f"O QuarterBack rating final é {qtRating}")