# [Ex 14] Cálculo o tempo que um semáforo deve demorar para abrir após o anterior ser aberto

import math;

print("--------------------------------------------------------------------")
print("Calculo de abertura de semáforo")
print("--------------------------------------------------------------------\n")

print("Para fazer o cálculo, por favor informe os seguintes valores:")
distanciaSemaforos = int(input("Informe a distância do semaforo atual até o próximo semáforo (em metros):"))
velocidadePermitida = int(input("Informe a velocidade permitida na via (em km/h):"))
aceleracaoCarro = int(input("Informe a aceleração do carro (em m/s²):"))

if (distanciaSemaforos <= 0 or velocidadePermitida <= 0 or aceleracaoCarro <= 0):
    print("Informe valores válidos!")
else:
    percursoUm = (math.pow(velocidadePermitida, 2)/(2*aceleracaoCarro))
    tempoPerUm = math.sqrt((2*percursoUm)/aceleracaoCarro)

    percursoDois = distanciaSemaforos - percursoUm
    tempoPerDois = percursoDois/velocidadePermitida
    print(f'Distãncia 1: {percursoUm}m | Tempo: {tempoPerUm:.2f}s | Distância 2: {percursoDois}m | Tempo: {tempoPerDois:.2f}s \nDistância Total: {distanciaSemaforos}m | Tempo Total: {tempoPerUm+tempoPerDois:.2f}s')