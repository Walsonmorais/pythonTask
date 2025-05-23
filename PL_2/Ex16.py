# Solicita o nome ao utilizador
nome = input("Digite o seu nome: ")

# Verifica se o nome contém apenas letras
if nome.isalpha():
    # Se o nome for válido, imprime em maiúsculas
    print(f"O nome em maiúsculas é: {nome.upper()}")
else:
    print("O nome deve conter apenas letras.")
