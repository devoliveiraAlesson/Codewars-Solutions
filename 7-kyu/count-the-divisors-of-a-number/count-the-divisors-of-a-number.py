def divisors(n):
    qtd = 0
    for i in range (1,n+1):
        if n%i == 0:
            qtd += 1
    return qtd