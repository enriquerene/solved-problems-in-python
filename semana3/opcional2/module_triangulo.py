class Triangulo:
    def __init__ ( self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes ( self, trngl ):
        own_sides = [ self.a, self.b, self.c ].sort()
        tr_sides = [ trngl.a, trngl.b, trngl.c ].sort()
        ratios = [ trngl.a / self.a, trngl.b / self.b, trngl.c / self.c ]
        return ratios[ 0 ] == ratios[ 1 ] and ratios[ 0 ] == ratios[ 2 ]
