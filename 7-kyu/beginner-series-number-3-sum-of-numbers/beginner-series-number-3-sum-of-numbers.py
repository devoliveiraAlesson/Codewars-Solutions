def get_sum(*args):
    soma = [i for i in range(min(args), max(args) + 1)]
    return args[0] if len(set(args)) == 1 else sum(soma)