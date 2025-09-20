def queue_time(customers, n):
    if n and customers:
        caixas = customers[:n]
        customers = customers[n:]
    
        for cliente in customers:
            menor = caixas.index(min(caixas))
            caixas[menor] = caixas[menor] + cliente
        
        return max(caixas)
    return 0