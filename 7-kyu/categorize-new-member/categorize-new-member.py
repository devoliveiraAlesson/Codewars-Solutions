def open_or_senior(data):
    resultado = []
    for i in data:
        if i[0] >= 55 and i[1] >= 8:
            resultado.append("Senior")
        else:
            resultado.append("Open")
    return resultado