def sale_hotdogs(n):
    
    multiplicador = [100,95,90][(n>4) + (n>9)]
    
    return n * multiplicador