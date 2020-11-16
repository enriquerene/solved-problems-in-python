def non_increasing ( ls ):
    for i in range( len( ls ) - 1 ):
        if ls[ i ] < ls[ i + 1 ]:
            return False
    return True

def non_decreasing ( ls ):
    for i in range( len( ls ) - 1 ):
        if ls[ i + 1 ] < ls[ i ]:
            return False
    return True

def ordenada ( ls ):
    return non_decreasing( ls ) or non_increasing( ls )
