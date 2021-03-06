def prof_bonus(level):
    # need to somehow add together character class prof bonus to certain saving throws
    prof_bonus = None
 
    if level >= 4:
        prof_bonus = 2
    elif level >= 8:
        prof_bonus = 3
    elif level >= 12:
        prof_bonus = 4
    elif level >= 16:
        prof_bonus = 5
    elif level >=20:
        prof_bonus = 6

    return (prof_bonus)
