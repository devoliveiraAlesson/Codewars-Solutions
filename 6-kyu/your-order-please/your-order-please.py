def order(sentence):
    lista = []
    for word in sentence.split():
        for i in word:
            if i.isdigit():
                lista.append(i + word)
    lista.sort()        
    return " ".join(["".join(i[1:]) for i in lista])