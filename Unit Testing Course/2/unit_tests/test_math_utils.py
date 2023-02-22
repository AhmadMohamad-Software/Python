import unittest
from math_utils import addition,subtraction,is_even

class MyTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1,1),2)
        self.assertNotEqual(addition(1,1),3)

    def test_subtraction(self):
        self.assertEqual(subtraction(4,2),2)

    def test_is_even(self):
        self.assertFalse(is_even(5))
        self.assertTrue(is_even(4))

    def test_general(self):
        a = "ahmad"
        self.assertIsNotNone(a)