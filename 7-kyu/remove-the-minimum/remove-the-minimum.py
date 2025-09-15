def remove_smallest(numbers):
    lista = [i for i in numbers]
    lista.remove(min(lista)) if lista else []
    return lista