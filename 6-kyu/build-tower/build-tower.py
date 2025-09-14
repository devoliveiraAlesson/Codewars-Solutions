def tower_builder(n_floors):
    contador = 0
    caractere = n_floors * 2 - 1
    lista = []
    for i in range(n_floors):
        lista.append(f"{' ' * contador}{'*' * caractere}{' ' * contador}")
        caractere -= 2
        contador += 1
    lista.reverse()
    return lista