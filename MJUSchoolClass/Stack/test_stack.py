import unittest
from Stack import Stack

class TestStack(unittest.TestCase): # TestCase 클래스 상속

    def test_is_empty(self): # 함수 하나하나가 하나의 함수를 테스트 해주는 것임
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())

    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(),2)




if __name__ == '__main__':
    unittest.main()
