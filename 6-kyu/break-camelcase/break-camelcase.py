def solution(s):
    resultado = []
    for i in s:
        if i == i.upper():
            resultado.append(" "+i)
        else:
            resultado.append(i)
    return "".join(i for i in resultado)