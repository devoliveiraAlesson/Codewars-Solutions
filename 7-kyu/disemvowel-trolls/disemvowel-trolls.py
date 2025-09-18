def disemvowel(string_):
    texto = str.maketrans("", "", "aeiouAEIOU")
    return string_.translate(texto)