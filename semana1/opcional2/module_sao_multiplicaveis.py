def sao_multiplicaveis( m1, m2 ):
    cols_in_m1 = len( m1[ 0 ] )
    rows_in_m2 = len( m2 )
    return cols_in_m1 == rows_in_m2
