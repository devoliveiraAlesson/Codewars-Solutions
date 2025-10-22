def tribonacci(signature, n):
    while len(signature) < 3:
        signature.insert(0)
    for i in range(n - len(signature)):
        x = sum(signature[-3:])
        signature.append(x)
    return signature[:n]