# Define um texto multilinha usando três apóstrofos
texto = '''Python é uma linguagem de programação poderosa.
Ela é usada para desenvolvimento web, ciência de dados, automação e muito mais.
Com Python, você pode criar projetos incríveis!'''

# Solicita uma palavra ao utilizador
cada_palavra = input("Digite uma palavra para verificar se está no texto: ")

# Verifica se a palavra está presente no texto
if cada_palavra in texto:
    print("A palavra está presente no texto.")
else:
    print("A palavra NÃO está presente no texto.")
