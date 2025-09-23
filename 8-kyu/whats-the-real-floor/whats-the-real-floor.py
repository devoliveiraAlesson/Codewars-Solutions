def get_real_floor(n):
    resposta = [0,1,2]
    return n - resposta[(n>0)+(n>13)]