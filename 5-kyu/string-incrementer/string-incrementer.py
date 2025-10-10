def increment_string(strng):
    res = []
    for i in reversed(strng):
        if i.isnumeric():
            res.append(i)
        else: break
    res.reverse()
    
    if len(res):
        v = len(res)
        i = len(strng) - v
        res.insert(0, "10")
        valor = "".join(res)
        valor = str(int(valor) + 1)
    
        if len(valor) - 2 == v and valor[1] == "0":
            return f"{strng[:i]}{valor[2:]}"
        else:
            return f"{strng[:i]}{valor[1:]}"
    
    return f"{strng}1"
    
​