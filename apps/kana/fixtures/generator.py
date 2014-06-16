import romkan


romaji = [
    "A", "I", "U", "E", "O", "KA", "KI", "KU", "KE", "KO", "SA", "SI", "SU", "SE", "SO", "TA", "TI", "TU", "TE", "TO",
    "NA", "NI", "NU", "NE", "NO", "HA", "HI", "FU", "HE", "HO", "MA", "MI", "MU", "ME", "MO", "YA", "YU", "YO", "RA",
    "RI", "RU", "RE", "RO", "WA", "WO", "N", "GA", "GI", "GU", "GE", "GO", "ZA", "ZI", "ZU", "ZE", "ZO", "DA", "DI",
    "DU", "DE", "DO", "BA", "BI", "BU", "BE", "BO", "PA", "PI", "PU", "PE", "PO", "KYA", "KYU", "KYO", "SHA", "SHU",
    "SHO", "CHA", "CHU", "CHO", "NYA", "NYU", "NYO", "HYA", "HYU", "HYO", "MYA", "MYU", "MYO", "RYA", "RYU", "RYO",
    "GYA", "GYU", "GYO", "JA", "JU", "JO", "BYA", "BYU", "BYO", "PYA", "PYU", "PYO"
]

for i, char in enumerate(romaji):

    # print i, char

    is_plain = i < 46
    is_dakuten = (i >= 46 and i < 71) or (i >= 92)
    is_handakuten = (i >= 66 and i < 71) or (i >= 101)
    is_youon = i >= 71

    if is_plain:
        if char.endswith("A") or char.endswith("N"):
            gojuon_row = 0
        elif char.endswith("I"):
            gojuon_row = 1
        elif char.endswith("U"):
            gojuon_row = 2
        elif char.endswith("E"):
            gojuon_row = 3
        else:
            gojuon_row = 4

        if char.startswith("A") or char.startswith("I") or char.startswith("U") or char.startswith("E") \
                or char.startswith("O"):
            gojuon_col = 0
        elif char.startswith("K"):
            gojuon_col = 1
        elif char.startswith("S"):
            gojuon_col = 2
        elif char.startswith("T"):
            gojuon_col = 3
        elif char.startswith("N") and len(char) > 1:
            gojuon_col = 4
        elif char.startswith("H"):
            gojuon_col = 5
        elif char.startswith("M"):
            gojuon_col = 6
        elif char.startswith("Y"):
            gojuon_col = 7
        elif char.startswith("R"):
            gojuon_col = 8
        elif char.startswith("W"):
            gojuon_col = 9
        elif char.startswith("N") and len(char) == 1:
            gojuon_col = 10

    elif not is_youon and is_dakuten:
        if char.endswith("A"):
            gojuon_row = 0
        elif char.endswith("I"):
            gojuon_row = 1
        elif char.endswith("U"):
            gojuon_row = 2
        elif char.endswith("E"):
            gojuon_row = 3
        else:
            gojuon_row = 4

        if char.startswith("G"):
            gojuon_col = 0
        elif char.startswith("Z"):
            gojuon_col = 1
        elif char.startswith("D"):
            gojuon_col = 2
        elif char.startswith("B"):
            gojuon_col = 3
        elif char.startswith("P"):
            gojuon_col = 4
        else:
            gojuon_col = 5

    else:
        if char.endswith("A"):
            gojuon_row = 0
        elif char.endswith("U"):
            gojuon_row = 1
        else:
            gojuon_row = 2

        if char.startswith("K"):
            gojuon_col = 0
        elif char.startswith("G"):
            gojuon_col = 1
        elif char.startswith("S"):
            gojuon_col = 2
        elif char.startswith("J"):
            gojuon_col = 3
        elif char.startswith("C"):
            gojuon_col = 4
        elif char.startswith("N"):
            gojuon_col = 5
        elif char.startswith("H"):
            gojuon_col = 6
        elif char.startswith("B"):
            gojuon_col = 7
        elif char.startswith("P"):
            gojuon_col = 8
        elif char.startswith("M"):
            gojuon_col = 9
        else:
            gojuon_col = 10

    alt = None
    if i == 11:
        char = 'SHI'
        alt = '"SI"'
    elif i == 16:
        char = 'CHI'
        alt = '"TI"'
    elif i == 17:
        char = 'TSU'
        alt = '"TU"'
    elif i == 52:
        char = 'JI'
        alt = '"ZI"'
    elif i == 57:
        char = 'JI'
        alt = '"DI"'
    elif i == 58:
        char = 'ZU'
        alt = '"DU"'

    if alt is None:
        alt = 'null'

    fixture = '{ "model": "kana.character", "pk": %(pk)s, "fields": { "romaji": "%(romaji)s", ' \
              '"hiragana": "%(hiragana)s", "katakana": "%(katakana)s", "is_plain": %(is_plain)s,' \
              '"is_dakuten": %(is_dakuten)s, "is_handakuten": %(is_handakuten)s, "is_youon": %(is_youon)s,' \
              '"gojuon_row": %(gojuon_row)s, "gojuon_col": %(gojuon_col)s, "alternate_romaji": %(alt)s, ' \
              '"notes": null } },'
    args = {
        'pk': i, 'romaji': char, 'hiragana': romkan.to_hiragana(char), 'katakana': romkan.to_katakana(char),
        'is_plain': str(is_plain).lower(), 'is_dakuten': str(is_dakuten).lower(),
        'is_handakuten': str(is_handakuten).lower(), 'is_youon': str(is_youon).lower(),
        'gojuon_row': str(gojuon_row), 'gojuon_col': str(gojuon_col), 'alt': alt
    }

    print(fixture % args)
