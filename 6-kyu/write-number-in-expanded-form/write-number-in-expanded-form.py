def expanded_form(num):
    n = []
    r = str(num)
    while len(r) > 0:
        if r[0] != "0":
            n.append((r)[0] + ("0" * (len(r) - 1)))
            r = r[1:]
        else:
            r = r[1:]
    return " + ".join(n)
    