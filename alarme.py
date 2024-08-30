import time
import datetime


def alarme(hora):
    rodando = True

    while rodando:
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
        print(hora_atual)

        if hora_atual == hora:
            print("ACORDAAAAAAAAAAAAAA")

            rodando = False

        time.sleep(1)


if __name__ == "__main__":
    hora = input("Digite a hora do alarme (HH:MM:SS): ")
    alarme(hora)
