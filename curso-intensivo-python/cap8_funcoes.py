# CAPITULO 8

# Definir uma função
def greet_user(username):
    """Exibe uma saudação simples"""
    print("Hello, " + username.title() + "!")


greet_user("João")

# Função com argumentos posicionais
def describe_pet(animal_type, pet_name):
    """Exibe informação sobre um pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")
describe_pet("harry", "hamster")  # A posiçao importa
# saída com argumentos nomeados
describe_pet(animal_type="dog", pet_name="willie")
describe_pet(pet_name="willie", animal_type="dog")  # Não muda

# Função com valores defaults
def describe_pet(pet_name, animal_type="dog"):  # Muda a ordem do argumento
    """Exibe informação sobre um pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name="willie")
describe_pet(pet_name="willie", animal_type="cat")

# Diferentes chamadas equivalentes
# Um cachorro chamado willie
describe_pet("willie")
describe_pet(pet_name="willie")
# Um haster chamado harry
describe_pet("harry", "hamster")
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")


# Função com retorno de um valor simples
def get_format_name(first_name, last_name):
    """Devolve um nome completo formateado"""
    full_name = first_name + " " + last_name
    return full_name.title()


musican = get_format_name("jimi", "hendrix")
print(musican)

# Função com argumeto opcional
def get_format_name(first_name, last_name, middle_name=""):
    """Devolve um nome completo formateado"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musican = get_format_name("jimi", "lee", "hendrix")
print(musican)
musican = get_format_name("jimi", "hendrix")
print(musican)

# Função para devolver um dicionário com argumento opcional
def build_person(fisrt_name, last_name, age=""):
    """Devolve um dict com informações das pessoas"""
    person = {"fisrt": fisrt_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musican = build_person("jim", "hendrix")
print(musican)
musican = build_person("jim", "hendrix", age=35)
print(musican)

# Função com laço while
def get_format_name(first_name, last_name):
    """Devolve nome completo formateado de foma elegante"""
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nQual é seu nome completo")
    print("\nDigite 'q' em qualquer momento para sair")

    print("\nPor favor diga seu nome: ")
    f_name = input("Nome: ")
    if f_name == "q":
        break

    l_name = input("Sobrenome: ")
    if l_name == "q":
        break

    formated_name = get_format_name(f_name, l_name)
    print("\n Olá " + formated_name + "!")

# Como pasar uma lista para uma função
def greet_user(names):  # estou passando a lista
    """Exibe uma saudação simples para cada usuário da lista"""
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)


users = ["juan", "pedro", "marcelo"]
greet_user(users)

# Alterar uma lista em uma função
# sem funções
unprinted_designs = ["iphone_case", "robot_pendant", "dodecahedron"]
completed_models = []

while unprinted_designs:
    current_designs = unprinted_designs.pop()

    print("Printind model: " + current_designs)
    completed_models.append(current_designs)

print("\nOs siguintes modelos foram impresos:")
for complet_model in completed_models:
    print(complet_model)

# refatorando o código anterior em duas funções
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressaõ de cada design, até que não haja mais nenhum.
    Transfere cada designs para completed_models.
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()

        completed_models.append(current_designs)


def show_completed_models(completed_models):
    """Mostra todos os modelos impresos."""
    print("\nOs seguintes designs foram impresos:")
    for complet_model in completed_models:
        print(complet_model)


unprinted_designs = ["iphone_case", "robot_pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# Passar um número arbitrario de argumentos (*)
def make_pizza(*toppings):
    """Lista os ingredientes de uma pizza"""
    print("\nA pizza está sendo preparada com: ")
    for topping in toppings:
        print(topping)


make_pizza("pepperoni", "cheese", "tomato")
make_pizza("pepperoni", "cheese")


# Misturar argumentos posiscionais e arbitrários
def make_pizza(size, *toppings):
    """ Apresenta a pizza que estamos preparando"""
    print("\nMaking a " + str(size) + "-inch with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, "pepperoni", "cheese", "tomato")
make_pizza(14, "pepperoni", "cheese")

# Usar argumentos nomeados arbitrários **
def build_profile(fisrt, last, **user_info):
    """Constrói um dicionário cm todo o que sabemos do usuário"""
    profile = {}
    profile["fisrt_name"] = fisrt
    profile["last_name"] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "albert", "einstein", location="princeton", fields="physis"
)
print(user_profile)


# Excercçios
# 8.7 Album
def make_album(artist_name, album_title, number_tracks=""):
    album = {"artista": artist_name, "album": album_title}
    if number_tracks:
        album["number_tracks"] = number_tracks
    return album


album_one = make_album("tool", "parabola")
print(album_one)

# 8.8 Album de usuários
while True:
    print("\nCrie um album!")
    print("\nInsira 'q' em qualquer momento para sair")

    artist_name = input("\nDigite o nome do artista: ")
    if artist_name == "q":
        break
    album_title = input("\nInsira o título do album: ")
    if album_title == "q":
        break
    album = make_album(artist_name, album_title)
    print(album)


# 8.12 Sanduíches
def make_sandwich(*ingredients):
    """Lista os ingredientes de um lanche"""
    print("\nO lanche contém os seguintes ingredientes:")
    for ingredient in ingredients:
        print(ingredient)


make_sandwich("tomato", "bief", "cheese", "mayonaise")
