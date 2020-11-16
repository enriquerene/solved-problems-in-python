import unittest
from module_soma_matrizes import soma_matrizes

class TestSomaMatrizes( unittest.TestCase ):
    def test_soma_matrizes_compativeis( self ):
        m1 = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
        m2 = [ [ 2, 3, 4 ], [ 5, 6, 7 ] ]
        expected_m = [ [ 3, 5, 7 ], [ 9, 11, 13 ] ]
        m = soma_matrizes( m1, m2 )
        self.assertEqual( m, expected_m )

    def test_soma_matrizes_incompativeis( self ):
        m1 = [ [ 1 ], [ 2 ], [ 3 ] ]
        m2 = [ [ 2, 3, 4 ], [ 5, 6, 7 ] ]
        expected_m = False
        m = soma_matrizes( m1, m2 )
        self.assertEqual( m, expected_m )

if __name__ == "__main__":
    unittest.main()
