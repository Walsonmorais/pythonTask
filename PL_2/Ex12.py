# Solicita a frase ao utilizador
frase = input("Digite uma frase: ").lower()  # Usamos .lower() para considerar maiúsculas e minúsculas

# Inicializa o contador de vogais
contador_vogais = 0

# Lista das vogais
vogais = "aeiou"

# Conta as vogais na frase
for cada_letra in frase:
    if cada_letra in vogais:
        contador_vogais += 1

# Exibe o resultado
print(f"A frase contém {contador_vogais} vogais.")
