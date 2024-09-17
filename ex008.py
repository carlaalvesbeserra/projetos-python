# MENU

menu = {"pastel": 6.0,
        "coxinha": 4.0,
        "enroladinho": 5.0,
        "esfiha": 5.0,
        "refri": 3.0,
        "suco": 3.0}

pedido = []
total = 0

print("-------------- MENU --------------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("----------------------------------")

while True:
    comida = input("Selecione um item (x para sair): ").lower()
    if comida == "x":
        break
    elif menu.get(comida) is not None:
        pedido.append(comida)

print("----------- SEU PEDIDO ------------")

for comida in pedido:
    total += menu.get(comida)
    print(comida)

print()
print(f"Total: R$ {total:.2f}")
