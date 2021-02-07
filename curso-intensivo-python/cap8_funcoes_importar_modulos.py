# # CAPITULO 8

# Usar alias para uma função
from pizza import make_pizza as mp

mp(16, "pepperoni", "cheese", "tomato")
mp(12, "pineapple", "cheese", "onion")

# Usar alias no módulo
import pizza as p

p.make_pizza(16, "pepperoni", "cheese", "tomato")
p.make_pizza(12, "pineapple", "cheese", "onion")

# Importar todas as funções de um módulo
from pizza import *

make_pizza(16, "pepperoni", "cheese", "tomato")
make_pizza(12, "pineapple", "cheese", "onion")
