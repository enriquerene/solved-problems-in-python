import unittest
from module_sao_multiplicaveis import sao_multiplicaveis

class TestSomaMatrizes( unittest.TestCase ):
    def test_nao_sao_multiplicaveis( self ):
        m1 = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
        m2 = [ [ 2, 3, 4 ], [ 5, 6, 7 ] ]
        expected = False
        result = sao_multiplicaveis( m1, m2 )
        self.assertEqual( expected, result )

    def test_sao_multiplicaveis( self ):
        m1 = [ [ 1 ], [ 2 ], [ 3 ] ]
        m2 = [ [ 1, 2, 3 ] ]
        expected = True
        result = sao_multiplicaveis( m1, m2 )
        self.assertEqual( expected, result )

if __name__ == "__main__":
    unittest.main()
