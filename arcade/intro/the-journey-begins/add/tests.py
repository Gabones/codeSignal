import unittest
from add import add

class Testadd(unittest.TestCase):
    # test case 1
    def test_case1(self):
        self.assertEqual(add(param1=1, param2=2), 3)
    
    # test case 2
    def test_case2(self):
        self.assertEqual(add(param1=0, param2=1000), 1000)
    
    # test case 3
    def test_case3(self):
        self.assertEqual(add(param1=2, param2=-39), -37)

    # test case 4
    def test_case4(self):
        self.assertEqual(add(param1=99, param2=100), 199)
        
    # test case 5
    def test_case5(self):
        self.assertEqual(add(param1=-100, param2=100), 0)

    # test case 6
    def test_case6(self):
        self.assertEqual(add(param1=-1000, param2=-1000), -2000)