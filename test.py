import unittest
from main import add, subtract, multiply, divide, remainder

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 7), 10)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(20, 5), 4)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(10, 5), 0)
        self.assertEqual(remainder(0, 5), 0)

        self.assertEqual(remainder(-10, 3), 2)
        self.assertEqual(remainder(10, -3), -2)

        with self.assertRaises(ZeroDivisionError):
            remainder(10, 0)
        
if __name__ == '__main__':
    unittest.main()