import doctest


def fizz_buzz(numbers):
    """
    Given a list of integers:
    1. Replace all integers that are evenly divisible by 3
    with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 and 5 with
    "fizzbuzz"
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    """
    # Solução usando enumerate
    for i, n in enumerate(numbers):
        if n % 5 == 0 and n % 3 == 0:
            numbers[i] = "fizzbuzz"
        elif n % 3 == 0:
            numbers[i] = "fizz"
        elif n % 5 == 0:
            numbers[i] = "buzz"

    # Solução usando len
    # for i in range(len(numbers)):  # range é criado no tamanho da lista
    #    n = numbers[i]  # número
    #    if n % 3 == 0 and n % 5 == 0:
    #        numbers[i] = 'fizzbuzz'
    #    elif n % 3 == 0:
    #        numbers[i] = 'fizz'
    #    elif n % 5 == 0:
    #        numbers[i] = 'buzz'
