# CAPITULO 6

# Acessar aos valores de um dicionário
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # Pela chave

# Salvando os valores numa variável
new_points = alien_0['points']
print(f"Voce ganhou {new_points} pontos")

# Adicionando pares chave-valor
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Começar com um dicionário vazio
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modificar valores
alien_0 = {'color': 'green'}
print(f"O color do alien é {alien_0['color']}")

alien_0['color'] = 'blue'
print(f"O color do alien é {alien_0['color']}")

# Modificando velocidade do alienígena
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("posição x original: " + str(alien_0['x_position']))

# determina a distância que o alienígena deve se deslocar de acordo com a
# sua velocidade atual, move o alienígena para a direita
if alien_0['speed'] == 'slow':
    alien_0['x_increment'] = 1  # x_increment nova variável
elif alien_0['speed'] == 'medium':
    alien_0['x_increment'] = 2
else:
    alien_0['x_increment'] = 3

# nova posição atingida mais o incremento
alien_0['x_position'] = alien_0['x_position'] + alien_0['x_increment']
print("posição x nova: " + str(alien_0['x_position']))
print(alien_0)

# Removendo pares chaves-valor
alien_0 = {'color': 'green', 'point': 5}
del alien_0['color']  # Usar del para remoção permanente
print(alien_0)

# Dicionário de objetos semelhantes - Enquete
favorite_languages = {
    'manoel': 'python',
    'junior': 'java',
    'sarah': 'c',
    'gian': 'php',
}
print(
    "A linguagem favorita de junior é "
    + favorite_languages['junior'].title()
    + "."
)


# EXERCÍCIOS
# 6.1 Pessoa
person = {
    'first_name': 'Fernanda',
    'last_name': 'Rossetti',
    'age': 33,
    'city': 'Limeira',
}

print(
    "Se chama {} {} tem {} e mora em {}".format(
        person['first_name'],
        person['last_name'],
        person['age'],
        person['city'],
    )
)

# 6.2 Números favoritos
favorite_numbers = {
    'Manoel': 8,
    'Fernanda': 7,
    'Pedro': 3,
}
print("O número favorito de Pedro é " + str(favorite_numbers['Pedro']))

# 6.3 Glossário
glossario = {
    'Print': 'função para mostrar dados',
    'Title': 'função para converter primeira letra da palavra em maiúscula',
    'Lower': 'função para converter letras em minúsculas',
}
for k, v in glossario.items():  # Retorna os pares de chave-valor
    print("{}: {}".format(k, v))
