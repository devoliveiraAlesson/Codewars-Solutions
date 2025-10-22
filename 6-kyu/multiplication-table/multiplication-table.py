def multiplication_table(size):   
    res = []   
    for i in range(size):
        i += 1
        x = 0
        y = i
        subRes = []
        while x < size:
            subRes.append(y)
            y += i
            x += 1
        res.append(subRes)
    return res
        