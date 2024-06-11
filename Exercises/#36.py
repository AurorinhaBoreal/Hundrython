# [Ex 36] Escreva um programa pra fazer a classificação de um curso

print("--------------------------------------------------------------------")
print("Classificação do Curso ❄️")
print("--------------------------------------------------------------------\n")

arrayProvas = []

prova1 = int(input("Informe os pontos da prova 1:"))
prova2 = int(input("Informe os pontos da prova 2:"))
prova3 = int(input("Informe os pontos da prova 3:"))
prova4 = int(input("Informe os pontos da prova 4:"))
prova5 = int(input("Informe os pontos da prova 5:"))

if (prova1 >= 70):
    arrayProvas.append(1)
else:
     arrayProvas.append(0)

if (prova2 >= 70):
    arrayProvas.append(1)
else:
    arrayProvas.append(0)

if (prova3 >= 70):
    arrayProvas.append(1)
else:
    arrayProvas.append(0)

if (prova4 >= 70):
    arrayProvas.append(1)
else:
    arrayProvas.append(0)

if (prova5 >= 70):
    arrayProvas.append(1)
else:
    arrayProvas.append(0)

try:
    if (arrayProvas.index(0) != -1):
        if (arrayProvas[0] == 1 and arrayProvas[1] == 1 and arrayProvas[2] == 0 and arrayProvas[3] == 1 and arrayProvas[4] == 0):
            print("Vocẽ passou na classificação B!")
        elif (arrayProvas[0] == 1 and arrayProvas[1] == 1 and arrayProvas[2] == 1 and arrayProvas[3] == 0 and arrayProvas[4] == 0):
            print("Você passou na classificação C!")
        else:
            print("Você foi reprovado!")
except ValueError:
    print(f"Você passou na classificação A.")