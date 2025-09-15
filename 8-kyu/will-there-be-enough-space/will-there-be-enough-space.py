def enough(cap, on, wait):
    pos = cap - (on + wait)
    neg = (on + wait) - cap
    return  0 if pos > 0 else neg