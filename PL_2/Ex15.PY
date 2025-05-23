# Solicita uma lista de palavras ao utilizador
palavras = input("Digite algumas palavras separadas por espaços: ").split()

# Junta as palavras com um espaço entre elas
frase = ' '.join(palavras)

# Exibe a frase resultante
print(f"A frase formada é: {frase}")
