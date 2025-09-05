def find_short(s):
    comprimento = [len(i) for i in s.split()]
    comprimento.sort()
    return comprimento[0]