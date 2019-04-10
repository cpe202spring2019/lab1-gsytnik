import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = loc
        loc3 = Location("CHINA", 33.3, 30.2)
        loc4 = Location("WHAT", 35.3, -120.7)
        self.assertEqual(loc2, loc)
        self.assertNotEqual(loc3, loc)
        self.assertNotEqual(loc2, loc3)
        self.assertNotEqual(1, loc2)
        self.assertNotEqual(loc, loc4)
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
