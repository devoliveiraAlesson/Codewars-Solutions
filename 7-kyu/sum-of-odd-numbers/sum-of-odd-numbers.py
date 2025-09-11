def row_sum_odd_numbers(n):
    valorAtual = 1
    nLinha = 1
    
    while nLinha < n:
        i = 0
        while i < nLinha:
            valorAtual += 2
            i += 1
        nLinha += 1
    
    linha = []
    while len(linha) < n:
        linha.append(valorAtual)
        valorAtual += 2
    
    return sum(linha)
        