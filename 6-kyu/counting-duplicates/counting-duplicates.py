def duplicate_count(text):
    dict = {}
    for i in text.lower():
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return sum(j > 1 for i, j in dict.items())
     