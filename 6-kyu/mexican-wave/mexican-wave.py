def wave(people):
    valorReal = people.replace(" ", "")
    lista = []
    idx = 0
    
    for letter in range(len(valorReal)):
        while people[idx] == " " and idx < len(people):
            idx += 1
        people = people[:idx] + people[idx].upper() + people[idx + 1:]
        lista.append(people)
        people = people.lower()
        idx += 1
    return lista
        