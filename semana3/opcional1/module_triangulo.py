class Triangulo:
    def __init__ ( self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c

    def sides_in_list ( self ):
        sides_list = [ self.a, self.b, self.c ]
        sides_list.sort()
        return sides_list

    def get_hypotenuse ( self ):
        return self.sides_in_list()[ 2 ]

    def get_catetes ( self ):
        return self.sides_in_list()[ :2 ]

    def get_square ( self, a ):
        return a ** 2

    def retangulo ( self ):
        cats = self.get_catetes()
        square_hyp_must_be = self.get_square( cats[ 0 ] ) + self.get_square( cats[ 1 ] )
        square_hyp_is = self.get_square( self.get_hypotenuse() ) 
        return square_hyp_must_be == square_hyp_is
