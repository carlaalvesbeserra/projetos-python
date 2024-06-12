# CONVERSOR DE TEMPERATURA

unidade = input("A temperatura é em Celsius ou Fahrenheit (C/F): ")
temperatura = float(input("Digite a temperatura: "))

if unidade == "C":
    temperatura = round((9 * temperatura) / 5 + 32, 1)
    print(f"A temperatura em Fahrenheit é: {temperatura}°F")
elif unidade == "F":
    temperatura = round((temperatura - 32) * 5 / 9, 1)
    print(f"A temperatura em Celsius é: {temperatura}°C")
else:
    print(f"{unidade} não é uma unidade válida")
