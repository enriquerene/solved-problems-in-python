import unittest
from module_triangulo import Triangulo
class TestTriangulo ( unittest.TestCase ):
    def test_triangle_not_similar ( self ):
        a = 1
        expected = False
        triangle = Triangulo( a, a, a )

        self.assertEqual( expected, triangle.semelhantes( Triangulo( a, a, a + 1 ) ) )

    def test_triangle_similar ( self ):
        a = 2
        b = 2 * a
        expected = True
        triangle = Triangulo( a, a, a )

        self.assertEqual( expected, triangle.semelhantes( Triangulo( b, b, b ) ) )

if __name__ == "__main__":
    unittest.main()
