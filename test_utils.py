# test_utils.py
import unittest
from utils import StringUtils

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(StringUtils.reverse_string("hello"), "olleh")
        self.assertEqual(StringUtils.reverse_string("123"), "321")

    def test_capitalize_string(self):
        self.assertEqual(StringUtils.capitalize_string("hello"), "HELLO")
        self.assertEqual(StringUtils.capitalize_string("HeLlO"), "HELLO")

    def test_lowercase_string(self):
        self.assertEqual(StringUtils.lowercase_string("HELLO"), "hello")
        self.assertEqual(StringUtils.lowercase_string("HeLlO"), "hello")

if __name__ == '__main__':
    unittest.main()
