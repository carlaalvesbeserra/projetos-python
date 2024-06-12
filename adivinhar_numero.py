# ADIVINHAR O NÚMERO

import random

tentativas = 0
numero = random.randint(1, 100)

while True:
   tentativa = int(input(f"Digite um número entre (1 - 100): "))
   tentativas += 1
   if tentativa < numero:
       print(f"{tentativa} é muito baixo")
   elif tentativa > numero:
       print(f"{tentativa} é muito alto")
   else:
       print(f"{tentativa} está correto!")
       break

print(f"Seu número de tentativas foram: {tentativas}")
