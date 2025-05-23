# Solicita a palavra ao utilizador
palavras = input("Digite uma palavra: ")

# Remove espaços antes de verificar, pois espaços não são letras
palavra_sem_espacos = palavras.replace(" ", "")

# Verifica se a palavra contém apenas letras
if palavra_sem_espacos.isalpha():
    print("A palavra contém apenas letras.")
else:
    print("A palavra NÃO contém apenas letras.")
