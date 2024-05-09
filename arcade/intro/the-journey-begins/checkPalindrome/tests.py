import unittest
from checkPalindrome import solution

class TestPalindrome(unittest.TestCase):
    # test case 1
    def test_case1(self):
        self.assertEqual(solution(inputString='aabaa'), True)
    
    # test case 2
    def test_case2(self):
        self.assertEqual(solution(inputString='abac'), False)
    
    # test case 3
    def test_case3(self):
        self.assertEqual(solution(inputString='a'), True)

    # test case 4
    def test_case4(self):
        self.assertEqual(solution(inputString='az'), False)
        
    # test case 5
    def test_case5(self):
        self.assertEqual(solution(inputString='abacaba'), True)

    # test case 6
    def test_case6(self):
        self.assertEqual(solution(inputString='z'), True)
    
    # test case 7
    def test_case7(self):
        self.assertEqual(solution(inputString='aaabaaaa'), False)
    
    # test case 8
    def test_case8(self):
        self.assertEqual(solution(inputString='zzzazzazz'), False)
    
    # test case 9
    def test_case9(self):
        self.assertEqual(solution(inputString='hlbeeykoqqqqokyeeblh'), True)
    
    # test case 10
    def test_case10(self):
        self.assertEqual(solution(inputString='hlbeeykoqqqokyeeblh'), True)
    