def title_case(title, minor_words=''):
    res = []
    
    for j,i in enumerate(title.lower().split(" ")):
        if j == 0 or i not in minor_words.lower().split():
            try:
                res.append(i.title())
            except:
                res.append(i)
        else:
            try:
                res.append(i.lower())
            except:
                res.append(i)
    return " ".join(res)
    