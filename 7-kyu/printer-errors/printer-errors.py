def printer_error(s):
    count = 0
    for i in s:
        if i > "m":
            count += 1
    return f"{count}/{len(s)}"