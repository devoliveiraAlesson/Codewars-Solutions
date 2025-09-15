def duplicate_encode(word):
    resposta = ""
    for i in word.lower():
        if word.lower().count(i) > 1:
            resposta += ")"
        else:
            resposta += "("
    return resposta