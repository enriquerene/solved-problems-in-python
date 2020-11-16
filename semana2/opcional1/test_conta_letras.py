import unittest
from module_conta_letras import conta_letras

class TestContaLetras( unittest.TestCase ):
    def test_conta_letras_vogais_implicitamente( self ):
        frase = "programamos em python"
        expected = 6
        resultado = conta_letras( frase )

        self.assertEqual( resultado, expected )

    
    def test_conta_letras_vogais_explicitamente( self ):
        frase = "programamos em python"
        expected = 6
        resultado = conta_letras( frase, "vogais" )

        self.assertEqual( resultado, expected )
    
    def test_conta_letras_consoantes( self ):
        frase = "programamos em python"
        expected = 13
        resultado = conta_letras( frase, "consoantes" )

        self.assertEqual( resultado, expected )


if __name__ == "__main__":
    unittest.main()
