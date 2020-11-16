import unittest
from module_primeiro_lex import primeiro_lex

class TestPrimeiroLex( unittest.TestCase ):
    def test_primeiro_lex_um( self ):
        letters1 = [ "olá", "A", "a", "casa" ]
        letters2 = [ "AAAAAA", "b" ]
        expected1 = "A"
        expected2 = "AAAAAA"
        resultado1 = primeiro_lex( letters1 )
        resultado2 = primeiro_lex( letters2 )

        self.assertEqual( resultado1, expected1 )
        self.assertEqual( resultado2, expected2 )
    

if __name__ == "__main__":
    unittest.main()
