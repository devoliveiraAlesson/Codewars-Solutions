def persistence(n, iter=0):
    if n < 10:
        return 0
    else:
        n = [int(i) for i in str(n)]
        resultado = 1
        for i in n:
            resultado *= i
        if resultado <10:
            return iter + 1
        else:
            return persistence(resultado, iter+1)