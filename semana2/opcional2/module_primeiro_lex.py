def primeiro_lex ( lista ):
    smallest = ""
    for item in lista:
        if item < smallest or smallest == "":
            smallest = item
    return smallest
