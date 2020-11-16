import unittest
from module_busca import busca

class TestBusca ( unittest.TestCase ):
    def test_not_found ( self ):
        _list = [ 'a', 'e', 'i' ]
        item = 'e'
        expect = 1
        self.assertEqual( expect, busca( _list, item ) )

    def test_found ( self ):
        _list = [ 12, 13, 14 ]
        item = 15
        expect = False
        self.assertEqual( expect, busca( _list, item ) )

if __name__ == "__main__":
    unittest.main()
