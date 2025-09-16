def high(x):
    dicionario = " abcdefghijklmnopqrstuvwxyz"
    dicionario = dict(enumerate([i for i in dicionario]))
    dicionario = {valor:chave for chave,valor in dicionario.items()}
    resposta = {}
    for word in x.split():
        r = 0
        for letter in word:
            r += dicionario[letter]
        if r not in resposta:
            resposta[r] = word
    return resposta[max(resposta)]
​