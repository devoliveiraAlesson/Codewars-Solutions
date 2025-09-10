def rot13(message):
    lista = "abcdefghijklmnopqrstuvwxyz"
    resultado = []
    for char in message:
        match char:
            case i if i in lista:
                resultado.append(lista[lista.index(i) - 13])
            case i if i in lista.upper():
                resultado.append(lista[lista.index(i.lower()) - 13].upper())
            case _:
                resultado.append(i)
    return "".join(resultado)
​