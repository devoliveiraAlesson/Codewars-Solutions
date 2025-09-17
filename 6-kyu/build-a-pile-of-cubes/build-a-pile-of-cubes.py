def find_nb(m):
    n =  0
    bloco = 0
    while n < m:
        n += bloco ** 3
        bloco += 1 if n != m else 0
    return bloco if n == m else -1