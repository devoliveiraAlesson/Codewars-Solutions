def get_middle(s):
    
    impar = s[len(s)//2]
    par = s[len(s)//2 - 1] + s[len(s)//2]
    
    if len(s)%2:
        return impar
    elif len(s) == 1:
        return s
    else:
        return par
    