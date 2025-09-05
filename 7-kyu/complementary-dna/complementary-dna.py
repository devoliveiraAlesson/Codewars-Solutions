def DNA_strand(dna):
    dicionario = {"A": "T", "C":'G', 'T': 'A', 'G':'C'}
    lista = []
    for i in dna:
        lista.append(dicionario[i])
    return "".join(lista)