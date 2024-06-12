# FATIADOR DE EMAIL

email = input("Digite seu email: ")
index = email.index("@")
username = email[:index]
dominio = email[index + 1:]

print(f"Seu nome de usuário é: {username}")
print(f"O domínio é: {dominio}")