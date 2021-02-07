def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar"""
    print("\nMake a " + str(size) +
          "-inch pizza whith following toppings:")
    for topping in toppings:
        print(topping)
