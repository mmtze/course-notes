#  1. Formas de aplicar uma função numa lista
lista = [1, 2, -5, 4]

# 1.1 Primeiro exemplo
def square(x):
    return x * x


forma_one = list(map(square, lista))

forma_two = []
for n in lista:
    forma_two.append(square(n))

forma_three = [square(x) for x in lista]  # Forma pythonica

print(forma_one)
print(forma_two)
print(forma_three)

# 1.2 Segundo exemplo
def is_odd(x):
    return x % 2 == 1


forma_one = list(filter(is_odd, lista))
forma_three = [x for x in lista if is_odd(x)]

print(forma_one)
print(forma_three)


# 1.3 Terceiro exemplo - Criação de uma matriz
'''
grid = [[0,0,0],
        [0,0,0]]
'''

# Criação normal
num_rows = 2
num_columns = 3
grid = []

for _ in range(num_rows):
    curr_now = []
    for _ in range(num_columns):
        curr_now.append(0)  # 3 loops [0,0,0]
    grid.append(curr_now)

print(grid)
# [[0, 0, 0], [0, 0, 0]]

# Forma pythonica
grig = [[0 for _ in range(num_rows)] for _ in range(num_columns)]
print(grid)


# 2. Usando as funções Built-In
lista = [1, 2, -5, 4]

num_max = max(lista)
print(num_max)
# 4

num_raiz_maior = max(lista, key=lambda x: x * x)
print(num_raiz_maior)
# -5

mod_2 = [(lambda x: x % 2 == 0)(num) for num in lista]
print(mod_2)
# [True, False, True, False]

# any() Retorna True se qualquer item em um iterável for verdadeiro
any_mod_2 = any([(lambda x: x % 2 == 0)(num) for num in lista])
print(any_mod_2)
# True

# all() Retorna True se todos os itens em um iterável forem verdadeiros
all_mod_2 = all([(lambda x: x % 2 == 0)(num) for num in lista])
print(all_mod_2)
# False
