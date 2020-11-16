import unittest
import io
import sys
from module_imprime_matriz import imprime_matriz

class TestImprimeMatriz( unittest.TestCase ):
    capturedOutput = None
    def setUp ( self ):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    
    def test_imprime_matriz_linha_maior_coluna( self ):
        minha_matriz = [ [ 1 ], [ 2 ], [ 3 ] ]
        expected_printStr = "1\n2\n3\n"
        
        imprime_matriz( minha_matriz )
        printStr = self.capturedOutput.getvalue()

        self.assertEqual( printStr, expected_printStr )

    
    def test_imprime_matriz_coluna_maior_linha( self ):
        minha_matriz = [ [ 1, 2, 3 ], [ 4 , 5, 6 ] ]
        expected_printStr = "1 2 3\n4 5 6\n"
        
        imprime_matriz( minha_matriz )
        printStr = self.capturedOutput.getvalue()
        
        self.assertEqual( printStr, expected_printStr )


if __name__ == "__main__":
    unittest.main()
