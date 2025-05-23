# Solicita a frase ao usuário
frase = input("Digite uma frase: ").strip()

# Verifica se começa com "Olá" usando split
primeira_palavra = frase.split(" ")[0]
comeca_frase = primeira_palavra == "Olá" or primeira_palavra == "Ola!" or primeira_palavra == "ola!"

# Verifica se termina com "!" sem usar endswith ou indexação
termina_frase = frase[-1:] == "!"

# Resultado
if comeca_frase:
    print("A frase começa com 'Olá")
elif termina_frase:
    print("A frase Termina com '!'.")
else:
    print("A frase NÃO começa com 'Olá' e NÃO termina com '!'.")
