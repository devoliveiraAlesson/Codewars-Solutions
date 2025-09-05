def high_and_low(numbers):
    lista = [int(i) for i in numbers.split()]
    return f"{max(lista)} {min(lista)}"