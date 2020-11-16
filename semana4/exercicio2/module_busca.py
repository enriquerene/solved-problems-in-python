def busca ( ls, item ):
    for i in range( len( ls ) ):
        if ls[ i ] == item:
            return i
    return False
