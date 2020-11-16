def dimensoes( matriz ):
    linhas = len( matriz )
    if linhas == 0:
        return print_dim( 0, 0 )
    cols = len( matriz[ 0 ] )
    print( str( linhas ) + "X" + str( cols ) ) 
