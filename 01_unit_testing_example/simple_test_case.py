"""This is an example of a very simpel test case."""

import unittest

def mult(a, b):
    return a * b

class TestMult(unittest.TestCase):
    def test_positive_number_multiplication(self):
        self.assertEqual(mult(2, 2), 4, "2 x 2 should be 4")

    def test_positive_negative_number_multiplication(self):
        self.assertEqual(mult(2, -2), -4, "2 x (-2) should be -4")

if __name__ == "__main__":
    unittest.main()
