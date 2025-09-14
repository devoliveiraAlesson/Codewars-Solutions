def delete_nth(order,max_e):
    dicionario = {i:0 for i in order}
    resposta = []
    for i in order:
        if dicionario[i] < max_e:
            dicionario[i] += 1
            resposta.append(i)
    return resposta
        