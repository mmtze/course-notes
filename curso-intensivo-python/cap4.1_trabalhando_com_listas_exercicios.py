# CAPITULO 4 - Exercícios

# 4.6 Números impares do 1 ao 20
for impar in range(1, 21, 2):
    print(impar)

# 4.7 Múltiplos de 3 do 3 ao 30
for multiplos in range(3, 31, 3):
    print(multiplos)

# 4.8 Cubos do 1 ao 10
cubo = []
for valor in range(1, 11):
    print("o cubo de {} é {}".format(valor, valor ** 3))
    cubo.append(valor ** 3)

print(cubo)

# 4.9 Cubos do 1 ao 10 com List Comprehension
cubos = [valor ** 3 for valor in range(1, 11)]
print(cubos)

# 4.10 Usando as fatias
minhas_comidas = [
    'pizza',
    'lanche',
    'suko',
    'carne',
    'pão',
    'salada',
    'cerveja',
]

print("Os três primeiros itens são:")
for comida in minhas_comidas[:3]:
    print(comida.title())

print("Os itens do meio são:")
for comida in minhas_comidas[2:5]:
    print(comida.title())

print("Os três últimos itens são:")
for comida in minhas_comidas[-3:]:
    print(comida.title())

# 4.11  Copiar listas
my_pizzas = ['peperoni', 'calabresa', 'portuguesa', 'napolitana']
friend_pizzas = my_pizzas[:]  # friend_pizzas=my_pizzas não funciona!

my_pizzas.append('doce')
friend_pizzas.append('abacaxi')

print("Minhas pizzas favoritas são:")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nAs pizzas favoritas de meu amigo são:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# 4.13 Tuplas não mudam!
buffet = ('frango milanesa', 'picanha e fritas', 'lasanha', 'escondidinho')
print("Cardápio:")
for pratos in buffet:
    print(pratos)

# buffet[-1] = 'salada'  # Não funciona!

buffet = ('frango milanesa', 'picanha e fritas', 'lasanha', 'salada')
print("\nDepois da mudança de cardápio:")
for pratos in buffet:
    print(pratos)
