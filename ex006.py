# TEMPORIZADOR DE CONTAGEM REGRESSIVA

import time

tempo = int(input("Digite a quantidade de segundos: "))

for i in range(tempo, 0, -1):
    segundos = i % 60
    minutos = int(i / 60) % 60
    horas = int(i / 3600)
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)

print("FIM")

