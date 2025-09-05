def number(bus):
    count = 0
    for i in bus:
        count += i[0] - i[1]
    return count