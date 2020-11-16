def dimensoes( matriz ):
    linhas = len( matriz )
    if linhas == 0:
        return "0X0"
    cols = len( matriz[ 0 ] )
    return str( linhas ) + "X" + str( cols )

def soma_matrizes( m1, m2 ):
    if ( dimensoes( m1 ) != dimensoes( m2 ) ):
        return False
    m = []
    for i in range( len( m1 ) ):
        m_linha = []
        for j in range( len( m1[ 0 ] ) ):
            m_linha.append( m1[ i ][ j ] + m2[ i ][ j ] )
        m.append( m_linha )
    return m
