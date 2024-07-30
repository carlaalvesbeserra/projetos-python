# CAÇA-NÍQUEL 🎰
import random


def giro():
    simbolos = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(simbolos) for _ in range(3)]


def print_rodada(rodada):
    print("*********************")
    print(" | ".join(rodada))
    print("*********************")


def pagamento(rodada, aposta):
    if rodada[0] == rodada[1] == rodada[2]:
        if rodada[0] == '🍒':
            return aposta * 5
        elif rodada[0] == '🍉':
            return aposta * 4
        elif rodada[0] == '🍋':
            return aposta * 3
        elif rodada[0] == '🔔':
            return aposta * 10
        elif rodada[0] == '⭐':
            return aposta * 100

    return 0


def main():
    saldo = 100

    print("--------------------------------")
    print("Bem-vindo ao Python Caça-Níqueis")
    print("🍒 🍉 🍋 🔔 ⭐")
    print("--------------------------------")

    while saldo > 0:
        print(f"Saldo atual: R$ {saldo}")
        print()

        aposta = input("Digite o valor da sua aposta: ")

        if not aposta.isdigit():
            print("Por favor digite um número válido!")
            continue

        aposta = int(aposta)

        if aposta > saldo:
            print("Saldo insuficiente")
            continue

        if aposta <= 0:
            print("A aposta tem que ser maior que 0")

        saldo -= aposta
        rodada = giro()

        print("Girando...")
        print_rodada(rodada)
        pag = pagamento(rodada, aposta)

        if pag > 0:
            print(f"Você ganhou R$ {pag}")
        else:
            print("Você perdeu essa rodada")

        saldo += pag
        jogar_novamente = input("Você quer jogar de novo?(S/N) ").upper()

        if jogar_novamente != "S":
            break

    print("---------------------------------------------")
    print(f"GAME OVER! Seu saldo final foi de R$ {saldo}")
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
