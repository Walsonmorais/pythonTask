# Palavra correta para adivinhar
palavra_correta = "python"

# Loop que continua pedindo ao utilizador até ele acertar
while True:
    # Solicita a palavra ao utilizador
    palavra = input("Tente adivinhar a palavra secreta: ").lower()
    
    # Verifica se a palavra inserida está correta
    if palavra == palavra_correta:
        print("Parabéns! Você acertou a palavra secreta!")
        break  # Sai do loop quando a palavra estiver correta
    else:
        print("Errado! Tente novamente.")
