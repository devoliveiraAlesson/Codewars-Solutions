def rgb(r, g, b):
    rgb = [max(0, min(255, i)) for i in [r,g,b]]
    lista = [hex(rgb[0]), hex(rgb[1]), hex(rgb[2])]
    temp = [(i[2:].zfill(2)) for i in lista]
    return "".join(temp).upper()