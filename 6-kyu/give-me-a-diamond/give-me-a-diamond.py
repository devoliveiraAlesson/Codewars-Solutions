def diamond(n):
    if n > 0 and n%2:
        asterisco = 1
        res = ""
        espaco = int(n/2)
        while asterisco < n:
            res += " " * espaco + "*" * asterisco + "\n"
            asterisco += 2
            espaco -= 1
        while asterisco >= 1:
            res += " " * espaco + "*" * asterisco + "\n"
            asterisco -= 2
            espaco += 1
        return res            
    else:
        return None