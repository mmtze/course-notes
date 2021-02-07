# CAPITULO 3

# Lista
nomes = ["manoel", "jão", "pedro", "alexandre"]
print(nomes)

# Acessar uma lista
print(nomes[0])  # Exibe "manoel"
print(nomes[0].title())  # Exibe "Manoel"

print(nomes[-1])  # Devolve o último valor da lista

# Usando os elementos da lista
print("Meu primeiro nome é " + nomes[0].title() + ".")
print("Meu segundo nome é " + nomes[2].upper() + ".")

# Alterar os elementos com o índice
motos = ["honda", "yamaha", "suzuki"]
motos[0] = "ducati"
print(motos)

# Acrescentando elementos na lista
motos.append("ducati")  # No final
print(motos)

motos.insert(2, "ducati")  # Em qualquer lugar usando a posisção
print(motos)

# Remover um elemento para sempre usando o indice
frutas = ["maça", "abacaxi", "limão", "laranja"]
print(frutas)

del frutas[0]  # Elimina o elemento sem poder usar de novo
print(frutas)

# Remover um elemento e poder retorná-lo
cor = ["branco", "azul", "preto", "amarelo"]
print(cor)
cor_apagado = cor.pop()  # Remove o último elemento (com índice: pop(0))
print(cor)
print(cor_apagado)  # Posso usar o elemento removido

# Remover um elemento usando o seu valor
coisas = ["mesa", "caneta", "copo", "mesa"]
print(coisas)
coisas.remove("mesa")  # Só apaga a primeira ocorrencia da lista
print(coisas)

# Organizar listas
carros = ["mazda", "fiat", "ford", "toyota"]
print(carros)
print(sorted(carros))  # Ordena apenas para apresentar
print(carros)
carros.sort()  # Ordena de forma permanente em ordem alfabética
print(carros)
carros.reverse()  # Organiza a lista ao inverso
print(carros)

# Tamanho de uma lista
eletricos = ["tomada", "plug", "conetor"]
print(len(eletricos))
