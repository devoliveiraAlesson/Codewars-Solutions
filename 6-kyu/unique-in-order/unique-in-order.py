def unique_in_order(sequence):
    resposta = []
    for i in sequence:
        if i not in resposta:
            resposta.append(i)
        else:
            if i != resposta[len(resposta) - 1]:
                resposta.append(i)
    return resposta