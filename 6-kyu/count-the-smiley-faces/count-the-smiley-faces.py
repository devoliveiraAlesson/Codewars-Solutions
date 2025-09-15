def count_smileys(arr):
    lista = [":)", ":D", ":-D",";~D", ":~)",";)", ";D", ";-D", ";~)"]
    contador = 0
    for i in arr:
        if i in lista:
            contador += 1
    print(arr)
    return contador