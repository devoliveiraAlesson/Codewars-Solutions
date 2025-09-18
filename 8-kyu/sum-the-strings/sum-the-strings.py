def sum_str(a, b):
    num = 0
    for i in [a,b]:
        if i:
            num += int(i)
    return str(num)
​