import unittest
from module_ordenada import ordenada

class TestOrdenada ( unittest.TestCase ):
    def test_not_ordered ( self ):
        unordered_list = [ 1, 5, 3 ]
        expect = False
        self.assertEqual( expect, ordenada( unordered_list ) )

    def test_not_decrease ( self ):
        ordered_list = [ 1, 1, 3 ]
        expect = True
        self.assertEqual( expect, ordenada( ordered_list ) )

    def test_not_increase ( self ):
        ordered_list = [ 4, 2, 2 ]
        expect = True
        self.assertEqual( expect, ordenada( ordered_list ) )

if __name__ == "__main__":
    unittest.main()
