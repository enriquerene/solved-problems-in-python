import unittest
from module_maiusculas import maiusculas

class TestMaiusculas( unittest.TestCase ):
    def test_maiusculas_apenas_uma( self ):
        frase = "Programamos em python 2?"
        expected = "P"
        resultado = maiusculas( frase )

        self.assertEqual( resultado, expected )

    
    def test_maiusculas_mais_de_uma( self ):
        frase1 = "Programamos em Python 3."
        frase2 = "PrOgRaMaMoS em python!"
        expected1 = "PP"
        expected2 = "PORMMS"
        resultado1 = maiusculas( frase1 )
        resultado2 = maiusculas( frase2 )

        self.assertEqual( resultado1, expected1 )
        self.assertEqual( resultado2, expected2 )


if __name__ == "__main__":
    unittest.main()
