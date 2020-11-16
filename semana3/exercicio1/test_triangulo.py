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

if __name__ == "__main__":
    unittest.main()
