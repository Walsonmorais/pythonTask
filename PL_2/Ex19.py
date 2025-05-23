# Definindo a frase
frase = input("Digite uma frase: ").split()
# Exibindo as três primeiras letras da frase
palavras = ''.join(frase)
tres_primeiras_letras = palavras[:3]
print("As três primeiras letras da frase são:", tres_primeiras_letras)
