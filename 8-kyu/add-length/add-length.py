def add_length(str):
    res = str.split()
    return [f"{i} {len(i)}" for i in res]