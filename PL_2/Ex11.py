# Solicita o raio do círculo ao utilizador
valor_raio = float(input("Digite o raio do círculo: "))

# Define o valor de pi
valor_pi = 3.14159

# Calcula a área do círculo
valor_area = valor_pi * valor_raio ** 2

# Imprime o resultado arredondado a duas casas decimais usando f-string
print(f"A área do círculo é: {valor_area:.2f} unidades quadradas.")
