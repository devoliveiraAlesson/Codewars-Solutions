def capitals(word):
    res = []
    for index, letra in enumerate(word):
        if letra.isupper():
            res.append(index)
            
    return res