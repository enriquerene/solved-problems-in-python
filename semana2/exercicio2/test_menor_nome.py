import unittest
from module_menor_nome import menor_nome

class TestMenorNome( unittest.TestCase ):
    def test_menor_nome_sem_espacos( self ):
        nomes = [ "maria", "josé", "PAULO", "Catarina" ]
        expected = "José"
        resultado = menor_nome( nomes )

        self.assertEqual( resultado, expected )

    def test_menor_nome_com_espacos( self ):
        nomes = [ "maria", " josé  ", "  PAULO", "Catarina  " ]
        expected = "José"
        resultado = menor_nome( nomes )

        self.assertEqual( resultado, expected )

    def test_menor_nome_com_empate( self ):
        nomes = [ "Bárbara", "JOSÉ  ", "Bill" ]
        expected = "José"
        resultado = menor_nome( nomes )

        self.assertEqual( resultado, expected )


if __name__ == "__main__":
    unittest.main()
