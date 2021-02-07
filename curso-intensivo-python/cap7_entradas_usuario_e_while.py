# CAPITULO 7

# Input - Entrada de usuário
nome = input("Digite seu nome: ")
print("Olá " + nome + "!")

# Prompts com mais de uma linha
prompt = "If you tell us who are, we can personalize the message you see"
prompt += "\nWhat's your name? "
nome = input(prompt)
print("Hello " + nome + "!")

idade = input("Digite sua idade: ")
idade = int(idade)
if idade > 18:
    print("Você é maior de idade!")
else:
    print("Você não é maior de idade!")

# Laço While - Contar de 1 até 5
numero = 1
while numero <= 5:
    print(numero)
    numero += 1

# Laço while - Usuário decide sair
prompt = "\nEscreva uma mensagem para eu repetir"
prompt += "\n(digite 'quit' para sair): "

active = True  # Usar uma flag no laço
while active:
    mensagem = input(prompt)  # Passando o prompt no laço
    if mensagem == "quit":
        active = False
    else:
        print(mensagem)

# Usar break no laço
prompt = "\nPor favor digite o nome de uma cidade que já visitou"
prompt += "\n(Coloque 'quit' para sair): "

activate = True
while activate:
    cidade = input(prompt)
    if cidade == 'quit':
        break
    else:
        print("Eu gostaria visitar também " + cidade)

# Usar continue no laço
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue  # Volta ao inicio
    print(numero)  # Só printa se número for impar


# Transferir dados entre listas
unconfirmed_users = ['alice', 'thomas', 'edith']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"verificando usuário: {current_user.title()}")
    confirmed_users.append(current_user)

print("Os siguintes usuários foram confirmados: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# Removendo todas as instâncias de valores especificos numa lista
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'python']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Prencher um dicionário com dados de um usuário
responses = {}
polling_active = True

while polling_active:
    name = input("Qual é seu nome?\n")
    response = input("Qual montanha você gostaria escalar algum dia?\n")

    # Armazena dados no dicionário
    responses[name] = response

    # Verifica se próxima pessoa vai responder
    repeat = input(
        "você gostaria de deixar outra pessoa responder (sim\não)?\n"
    )
    if repeat == 'não':
        polling_active = False

print("-------Resultados--------")
for name, response in responses.items():
    print(name + " gostaria escalar " + response)


# Exercícios
# 7.5 e 7.6 Ingresso para o cinema
prompt = "Qual é sua idade?\n"
prompt += "(Digite 'quit' para sair): "
activate = True
while activate:
    idade = input(prompt)
    if idade == 'quit':
        break
    elif int(idade) < 3:
        print("O ingresso é 5 dolares")
    elif int(idade) >= 3 and int(idade) <= 12:
        print("O ingesso é 10 dólares")
    elif int(idade) > 12:
        print("O ingresso é 15 dólares")


# 7.8 Lanchonete e 7.9 Removendo o pastrami
sandwich_order = ['pastrami', 'x bacon', 'x tudo', 'x salada', 'pastrami']
finished_sandwiches = []

print("O Pastrami está esgotado!")

# Removendo o pastrami
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    current_order = sandwich_order.pop()
    print(f"Preparei seu {current_order.title()}")

    finished_sandwiches.append(current_order)

print("Lanches preparados:")
for order in finished_sandwiches:
    print(order.title())
