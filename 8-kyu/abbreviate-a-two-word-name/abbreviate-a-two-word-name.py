def abbrev_name(name):
    nome = [i[0] for i in name.split()]
    return f"{nome[0].upper()}.{nome[1].upper()}"