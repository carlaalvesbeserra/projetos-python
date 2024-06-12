# CALCULADORA DE INVESTIMENTOS

valor_inicial = 0
taxa = 0
tempo = 0

while valor_inicial <= 0:
    valor_inicial = float(input("Digite o valor inicial: "))
    if valor_inicial <= 0:
        print("O valor inicial não pode ser menor ou igual a zero")

while taxa <= 0:
    taxa = float(input("Digite o valor da taxa em %: "))
    if taxa <= 0:
        print("A taxa não pode ser menor ou igual a zero")

while tempo <= 0:
    tempo = int(input("Digite o tempo em anos: "))
    if tempo <= 0:
        print("O tempo não pode ser menor ou igual a zero")

total = valor_inicial * pow((1 + taxa / 100), tempo)

print(f"Depois de {tempo} ano/s: R$ {total:.2f}")

