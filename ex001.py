# CALCULADORA

operador = input("Escolha um operador (+ - * /): ")
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))

if operador == "+":
    resultado = num1 + num2
    print(round(resultado, 3))
elif operador == "-":
    resultado = num1 - num2
    print(round(resultado, 3))
elif operador == "*":
    resultado = num1 * num2
    print(round(resultado, 3))
elif operador == "/":
    resultado = num1 / num2
    print(round(resultado, 3))
else:
    print(f"{operador} não é um operador válido")
