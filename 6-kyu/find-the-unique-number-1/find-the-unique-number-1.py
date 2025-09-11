def find_uniq(arr):
    dicionario = {}
    for i in set(arr):
        dicionario[arr.count(i)] = i
    dicionario = sorted(dicionario.items())
    return dicionario[0][1]