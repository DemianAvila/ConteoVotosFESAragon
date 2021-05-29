def caracteresEspeciales(s):
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ä", "a"),
        ("ë", "e"),
        ("ï", "i"),
        ("ö", "o"),
        ("ü", "u"),
    )
    for a, b in reemplazos:
        s = s.replace(a, b).replace(a.upper(), b.upper())
        s=s.upper()
    return s

# print(caracteresEspeciales("JoSüé DemíÄn"))