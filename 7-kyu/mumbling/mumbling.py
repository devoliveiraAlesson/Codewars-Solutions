def accum(st):
    str = []
    for i in range(len(st)):
        str.append(st[i] * (i+1))
    return "-".join(str).title()