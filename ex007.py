# Carrinho de compras

alimentos = []
precos = []
total = 0

while True:
    alimento = input("Digite o item que deseja comprar (x para sair): ").lower()
    if alimento == "x":
        break
    else:
        preco = float(input("Digite o preço: R$ "))
        alimentos.append(alimento)
        precos.append(preco)

print("----- SEU CARRINHO ------")

for alimento in alimentos:
    print(alimento)

for preco in precos:
    total += preco

print("-------------------------")
print(f"Total: R${total}")


