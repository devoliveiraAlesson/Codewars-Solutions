def is_triangle(a, b, c):
    if sum([a,b,c]) / 2 <= max([a,b,c]):
        return False
    else:
        return True