import math
def find_next_square(sq):
    result = math.sqrt(sq).is_integer()
    if result:
        teste = sq + 1
        while not math.sqrt(teste).is_integer():
            teste += 1
        return teste
            
    else:
        return -1
​