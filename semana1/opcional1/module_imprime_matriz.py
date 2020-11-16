def imprime_matriz ( matrix ):
    num_rows = len( matrix )
    num_cols = len( matrix[ 0 ] )
    for i in range( num_rows ):
        for j in range( num_cols ):
            if ( j < num_cols - 1 ):
                print( matrix[ i ][ j ], end=" " )
            else:
                print( matrix[ i ][ j ] )
