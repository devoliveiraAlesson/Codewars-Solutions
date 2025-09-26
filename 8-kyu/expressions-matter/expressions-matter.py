def expression_matter(a, b, c):
    res = [(a + b + c), (a * b * c), ((a+b)*c), (a*(b+c))]
    return max(res)