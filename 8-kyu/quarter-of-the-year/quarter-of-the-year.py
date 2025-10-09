def quarter_of(month):
    if month % 3:
        return month // 3 + 1
    else:
        return month / 3