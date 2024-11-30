import unittest
from calculator import subtract

class TestSubtract(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -5), -5)

    def test_subtract_with_zero(self):
        self.assertEqual(subtract(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
