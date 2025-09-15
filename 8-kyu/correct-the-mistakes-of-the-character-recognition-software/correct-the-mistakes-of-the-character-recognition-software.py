def correct(s):
    res = []
    for i in s:
        if i.isdigit():
            res.append(["O", "I", "S"][(int(i)>1) + (int(i)>0)])
        else: res.append(i)
    return "".join(res)