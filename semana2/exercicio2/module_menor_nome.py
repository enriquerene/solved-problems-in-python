def menor_nome ( nomes ):
    shortest_name = ""
    for i in range( len( nomes ) ):
        name = nomes[ i ]
        name = name.strip()
        name = name.lower()
        first_letter = name[ 0 ].capitalize()
        rest_of_name = name[ 1: ]
        name = first_letter + rest_of_name
        if ( len( name ) < len( shortest_name) or len( shortest_name ) == 0 ):
            shortest_name = name

    return shortest_name
