def array_intersection ( needle, haystack ):
    output = []
    for i in haystack:
        if i in needle:
            output.append( i )
    return output

def letters_as_array ( frase ):
    return list( frase.lower() )

def vowels ( frase ):
    vowels = [ "a", "e", "i", "o", "u" ]
    letters = letters_as_array( frase )
    return array_intersection( vowels, letters )

def consoants ( frase ):
    consoants = [ "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"  ]
    letters = letters_as_array( frase )
    return array_intersection( consoants, letters )

def conta_letras ( frase, contar = "vogais" ):
    if ( contar == "consoantes" ):
        return len( consoants( frase ) )
    return len( vowels( frase ) )
