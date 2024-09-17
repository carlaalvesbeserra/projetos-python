# CONVERSOR DE PESO

peso = float(input("Digite seu peso: "))
unidade = input("Quilogramas ou libras? (K or L): ")

if unidade == "K":
    peso = peso * 2.205
    unidade = "Lbs."
    print(f"Seu peso é: {round(peso, 1)} {unidade}")
elif unidade == "L":
    peso = peso / 2.205
    unidade = "Kgs."
    print(f"Seu peso é: {round(peso, 1)} {unidade}")
else:
    print(f"{unidade} não é uma unidade válida")
