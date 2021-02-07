# CAPITULO 4

# Extrair um nome da lista e o armazená-lo numa variável
magicos = ["alice", "david", "carolina"]
for x in magicos:
    print(x)

magicos = ["alice", "david", "carolina"]
for x in magicos:
    print(x.title() + " é um bom mago\n")

# Usando Range
for valor in range(1, 6):  # O último número não é considerado
    print(valor)

numeros = list(range(1, 6))  # Posso criar uma lista com list()
print(numeros)

numeros = list(range(2, 11, 2))  # O último valor determina que seja de 2 em 2
print(numeros)

quadrados = []
for valor in range(1, 11):
    quadrados.append(valor ** 2)  # Adiciona os valores
print(quadrados)

# List Comprehension
# Combinar o laçõ e a criação de novos elementos numa linha
quadrados = [valor ** 2 for valor in range(1, 11)]
print(quadrados)

# Mínimo, Máximo e Soma
digitos = list(range(1, 11))
print(min(digitos))
print(max(digitos))
print(sum(digitos))
