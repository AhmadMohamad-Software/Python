import unittest

from convert_utils import cm_to_m

class MyTest2(unittest.TestCase):
    def test_cm_to_m(self):
        result = cm_to_m(500)
        self.assertEqual(result,5.0)