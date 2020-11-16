import unittest
from module_triangulo import Triangulo
class TestTriangulo ( unittest.TestCase ):
    def test_instantiate ( self ):
        a, b, c = 1, 1, 1
        expected_perimeter = a + b + c
        triangle = Triangulo( a, b, c )

        self.assertEqual( a, triangle.a )
        self.assertEqual( b, triangle.b )
        self.assertEqual( c, triangle.c )
        self.assertEqual( expected_perimeter, triangle.perimetro() )

    def test_equilatero ( self ):
        a = 1
        triangle = Triangulo( a, a, a )

        self.assertEqual( "equilátero", triangle.tipo_lado() )

    def test_isosceles ( self ):
        a = 2
        b = 1
        triangle = Triangulo( a, a, b )

        self.assertEqual( "isósceles", triangle.tipo_lado() )

    def test_escaleno ( self ):
        a = 3
        b = 4
        c = 5
        triangle = Triangulo( a, b, c )

        self.assertEqual( "escaleno", triangle.tipo_lado() )


if __name__ == "__main__":
    unittest.main()
