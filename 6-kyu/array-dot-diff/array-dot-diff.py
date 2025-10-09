def array_diff(a, b):
    res = []
​
    for i in a:
        if i not in b:
            res.append(i)
    return res