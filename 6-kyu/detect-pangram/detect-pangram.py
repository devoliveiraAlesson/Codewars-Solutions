def is_pangram(st):
    conjunto = set()
    for i in st.lower():
        conjunto.add(i) if i.isalpha() else None
    return len(conjunto) == 26