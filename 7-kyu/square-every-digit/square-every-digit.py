def square_digits(num):
    lista = str(num)
    resposta = []
    for i in lista:
        resposta.append(str(int(i)**2))
    return int("".join(resposta))
    
​
    """
    lista = []
    while num > 0:
        lista.append(num % 10)
        num = num // 10
    lista.reverse()
    resposta = [i**2 for i in lista]
    return """