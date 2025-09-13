def count(s):
    dicionario = {}
    for i in s:
        if i not in dicionario:
            dicionario[i] = s.count(i)
    return dicionario