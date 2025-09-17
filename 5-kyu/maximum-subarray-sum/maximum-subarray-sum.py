def max_sequence(arr):
    valorAtual = 0
    valorMaximo = 0
    for i in arr:
        valorAtual += i
        if valorAtual > valorMaximo:
            valorMaximo = valorAtual
        elif valorAtual < 0:
            valorAtual = 0
    return valorMaximo