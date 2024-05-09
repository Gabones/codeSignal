import unittest
from centuryFromYear import solution

class TestCentury(unittest.TestCase):
    # test case 1
    def test_case1(self):
        self.assertEqual(solution(year=1905), 20)
    
    # test case 2
    def test_case2(self):
        self.assertEqual(solution(year=1700), 17)
    
    # test case 3
    def test_case3(self):
        self.assertEqual(solution(year=1988), 20)

    # test case 4
    def test_case4(self):
        self.assertEqual(solution(year=2000), 20)
        
    # test case 5
    def test_case5(self):
        self.assertEqual(solution(year=2001), 21)

    # test case 6
    def test_case6(self):
        self.assertEqual(solution(year=200), 2)
    
    # test case 7
    def test_case7(self):
        self.assertEqual(solution(year=374), 4)

    # test case 8
    def test_case8(self):
        self.assertEqual(solution(year=45), 1)

    # test case 9
    def test_case9(self):
        self.assertEqual(solution(year=8), 1)