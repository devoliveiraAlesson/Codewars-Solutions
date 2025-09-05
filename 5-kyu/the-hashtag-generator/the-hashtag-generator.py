def generate_hashtag(s):
    if len(s.replace(" ", "")) >= 140:
        return False
    if not s:
        return False
    else:
        return "#" + s.title().replace(" ", "")
​