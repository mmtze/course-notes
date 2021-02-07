# CAPITULO 2

nome = "ada lovelace"
print(nome.title())  # Letra maiúscula no inicio
print(nome.upper())  # Letras maiúsculas
print(nome.lower())  # Letras minussculas

# Concatenando
nome = "ada"
sobrenome = "lovelace"
nome_completo = nome + " " + sobrenome
print(nome_completo)
print(nome_completo.title())

# Acrescentando espaços
print("\tpython")  # Tabulada
print("python\nC\nC++\n")  # Outra linha

# Removendo espaços em branco
linguagem = " python  "
print(linguagem.lstrip())  # No começo
print(linguagem.rstrip())  # No final
print(linguagem.strip())  # Ambos lados

# Transformar um inteiro em string
idade = 33
print("Feliz " + str(idade) + " anos")
print("meu numero favoriot é " + str(idade))
