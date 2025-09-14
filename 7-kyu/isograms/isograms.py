def is_isogram(string):
    return not (len(set(string.lower())) - len(string.lower()))