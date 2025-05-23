# Exercicio 2

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

palavra = input("Digite a palavra que deseja verificar: ")

palavras_na_frase = frase.split()

palavras_na_frase = [p for p in palavras_na_frase if p.isalpha()]

if palavra in palavras_na_frase:
    print(f"A palavra '{palavra}' existe na frase.")
else:
    print(f"A palavra '{palavra}' NÃO existe na frase.")