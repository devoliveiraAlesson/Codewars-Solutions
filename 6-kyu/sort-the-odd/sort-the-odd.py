def sort_array(array):
    lista = [i for i in array if i%2]
    lista.sort()
    novaLista = []
    for i in array:
        if i%2:
            novaLista.append(lista[0])
            lista.pop(0)
        else:
            novaLista.append(i)
    return novaLista