# CAPITULO 5 - Exercícios

# Comparando valores
car = "Audi"
print(car == "audi")
print(car.lower() == "audi")  # Não altera o original

# Confere se elemento está na lista
lista = ["a", "b", "c", "d"]
print("a" in lista)

# 5.3 Cores de alienígenas #1
alien_color = "green"
if alien_color == "green":
    print("Você ganhou 5 pontos")

# 5.4 Cores de alienígenas #2
alien_color = "yellow"
if alien_color == "red":
    print("Você ganhou 5 pontos")
else:
    print("Você ganhou 10 pontos")

# 5.5 Cores de alienígenas #3
alien_color = "yellow"
if alien_color == "green":
    print("Você ganhou 5 pontos")
elif alien_color == "yellow":
    print("Você ganhou 10 pontos")
else:  # Poderia ser também: elif alien_color == 'red'
    print("Você ganhou 25 pontos")

# 5.6 Estágios da vida
age = int(input("Qual é sua idade = "))
if age < 2:
    print("Você é um bebê")
elif age < 4:  # 2 a 4 pois é uma cadeia
    print("Você é uma criança")
elif age < 13:
    print("Você é um(a) garoto(a)")
elif age < 20:
    print("Você é um(a) adolescente")
elif age < 65:
    print("Você é um adulto")
else:
    print("Você é um idoso")

# 5.7 Fruta favorita
favorite_fruits = ["pera", "uva", "melão"]
if "pera" in favorite_fruits:
    print("Você realmente gosta das peras!")
if "uva" in favorite_fruits:
    print("Você realmente gosta da uvas!")
if "melão" in favorite_fruits:
    print("Você realmente gosta da melão!")
if "melancia" in favorite_fruits:
    print("Você realmente gosta da melancia!")


# 5.8 e 5.9 Lista de usuários
usuarios = ['admin', 'manoel', 'bianca', 'pedro']
usuarios = []
if usuarios:  # Verifica se está vazia, é true se tem algum item
    for usuario in usuarios:
        if usuario == "admin":
            print("Olá admin, gostaria ver alguns relatórios")
        else:
            print(f"Olá {usuario}, obrigado por fazer login novamente")
else:
    print("Precisamos encontrar alguns usuários")

# 5.10 Verificando nomes de usuários
current_user = ["juan", "maria", "fernanda", "junior", "thiago"]
new_user = ["manoel", "roberta", "junior", "rodrigo", "joão"]
for user in new_user:
    user = user.lower()  # Não altera permanentemente
    if user in current_user:
        print("Usuário já usado, informe um novo nome")
    else:
        print("Usuário está disponível")

# 5.11 Números ordinais
ordinais = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in ordinais:
    if numero == 1:
        print(str(numero) + "st")
    elif numero == 2:
        print(str(numero) + "nd")
    else:
        print(str(numero) + "th")
