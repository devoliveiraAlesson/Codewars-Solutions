def filter_list(l):
    lista = []
    for i in l:
        if isinstance(i, int) and i not in lista:
            lista.append(i)
    return lista