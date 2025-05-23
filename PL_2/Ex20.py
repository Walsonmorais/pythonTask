# Definindo a frase
frase = input("Digite uma frase: ").split()
# Exibindo as 5 últimas letras da frase
palavras = ''.join(frase)
cinco_ultimas_letras = palavras[-5:]
print("As cinco últimas letras da frase são:", cinco_ultimas_letras)