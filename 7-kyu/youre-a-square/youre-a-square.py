def is_square(n):
    if n >= 0:
        return round(n ** 0.5) == n**0.5
    else:
        return False