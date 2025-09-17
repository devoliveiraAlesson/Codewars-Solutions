def binary_array_to_number(arr):
    lista = []
    for ind,num in enumerate(reversed(arr)):
        lista.append(2**ind * num)
    return sum(lista)