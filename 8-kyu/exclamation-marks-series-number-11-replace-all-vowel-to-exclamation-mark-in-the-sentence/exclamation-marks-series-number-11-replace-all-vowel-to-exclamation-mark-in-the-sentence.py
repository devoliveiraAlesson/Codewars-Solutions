def replace_exclamation(st):
    translatetable = str.maketrans("aeiouAEIOU", "!!!!!!!!!!")
    return st.translate(translatetable)