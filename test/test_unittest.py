import unittest
from src.calculator import add_numbers, subtract_numbers, multiply_numbers, divide_numbers, combined_operation


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add_numbers(4, 2), 6)

    def test_subtract(self):
        self.assertEqual(subtract_numbers(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply_numbers(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide_numbers(10, 2), 5)

    def test_combined(self):
        self.assertEqual(combined_operation(3, 2), (5 + 1 + 6))


if __name__ == "__main__":
    unittest.main()
