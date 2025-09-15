def dir_reduc(arr):
    
    lista = "".join([i[0] for i in arr])
    pre = len(lista)
    pos = 0
    while pre > pos:
        pre = len(lista)
        lista = lista.replace("NS","")
        lista = lista.replace("SN", "")
        lista = lista.replace("WE", "")
        lista = lista.replace("EW", "")
        pos = len(lista)
    res = []
    dicionario = {"N":"NORTH", "S":"SOUTH", "W":"WEST", "E":"EAST"}
    
    for i in lista:
        res.append(dicionario[i])
    
    return res