class Triangulo:
    def __init__ ( self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c

    def perimetro ( self ):
        return self.a + self.b + self.c

    def how_many_are_equal ( self ):
        if self.a == self.b and self.a == self.c:
            return 3
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return 2
        return 1

    def tipo_lado ( self ):
        equals = self.how_many_are_equal()
        if equals == 3:
            return "equilátero"
        elif equals == 2:
            return "isósceles"
        else:
            return "escaleno"
        
        
        
