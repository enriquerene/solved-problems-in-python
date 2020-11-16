import unittest
from module_triangulo import Triangulo
class TestTriangulo ( unittest.TestCase ):
    def test_triangle_not_rectangle ( self ):
        a, b, c = 1, 3, 5
        expected = False
        triangle = Triangulo( a, b, c )

        self.assertEqual( expected, triangle.retangulo() )

    def test_triangle_not_rectangle_equi ( self ):
        a = 3
        expected = False
        triangle = Triangulo( a, a, a )

        self.assertEqual( expected, triangle.retangulo() )

    def test_triangle_rectangle ( self ):
        a, b, c = 3, 4, 5
        expected = True
        triangle = Triangulo( a, b, c )

        self.assertEqual( expected, triangle.retangulo() )

if __name__ == "__main__":
    unittest.main()
