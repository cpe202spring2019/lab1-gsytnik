import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests an iteration loop which find the largest value in a list
        and returns that value"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        tlist = []
        self.assertEqual(None, max_list_iter(tlist))
        t1 = [1,1,1,3,4,20,3,4,20,21]
        t2 = [1,2,3,4,5,6,20,20]
        t3 = [-1,-20,-10,-20,-10]
        t4 = [3,3,3,3]
        self.assertEqual(max_list_iter(t1), 21)
        self.assertEqual(max_list_iter(t2), 20)
        self.assertEqual(max_list_iter(t3), -1)
        self.assertEqual(max_list_iter(t4), 3)
        self.assertEqual(max_list_iter([1], 1)

    def test_reverse_rec(self):
        """tests a recursive loop which returns the reversed list."""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([5,4,3,2,1]),[1,2,3,4,5])
        self.assertEqual(reverse_rec([0,0,0,0,1]),[1,0,0,0,0])
        self.assertEqual(reverse_rec([]), [] )

    def test_bin_search(self):
        """tests binary search recursive loop"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        l1 = 2
        l2 = 1
        l3 = 7
        h1 = 3
        h2 = 7
        h3 = 8
        list2 = [1,2,3,4,5,6,7,8,9,10,11]
        self.assertEqual(bin_search(4, l1, h1, list_val), None )
        self.assertEqual(bin_search(6, l2, h2, list2), 5 )
        self.assertEqual(bin_search(4, l3, h3, list_val), None )

if __name__ == "__main__":
        unittest.main()

    
