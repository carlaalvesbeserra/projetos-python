# JOGO PEDRA, PAPEL OU TESOURA

import random

opcoes = ("pedra", "papel", "tesoura")
jogando = True

while jogando:
    usuario = None
    pc = random.choice(opcoes)

    while usuario not in opcoes:
        usuario = input("Escolha entre (pedra, papel ou tesoura): ")

    print(f"Usuário: {usuario}")
    print(f"PC: {pc}")

    if usuario == pc:
        print("EMPATOU!")
    elif usuario == "pedra" and pc == "tesoura":
        print("VOCÊ VENCEU!")
    elif usuario == "papel" and pc == "pedra":
        print("VOCÊ VENCEU!")
    elif usuario == "tesoura" and pc == "papel":
        print("VOCÊ VENCEU!")
    else:
        print("VOCÊ PERDEU!")

    if not input("Jogar de novo? (s/n): ").lower() == "s":
        running = False

print("FIM DE JOGO")