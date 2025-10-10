def dig_pow(n, p):
    m = str(n)
    m = [i for i in m]
    
    pow = []
    
    for i in m:
        pow.append(int(i)**p)
        p += 1
    pow = sum(pow)
    
    if pow % n:
        return -1
    else:
        return pow / n