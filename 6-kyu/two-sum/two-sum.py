def two_sum(numbers, target):
    resposta = []
    for idx,i in enumerate(numbers):
        for nidx, j in enumerate(numbers):
            if idx != nidx:
                if i + j == target:
                    resposta.append(idx)
                    resposta.append(nidx)
    print(resposta)
    return (resposta[0], resposta[1])
            