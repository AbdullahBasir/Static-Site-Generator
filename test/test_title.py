from title import extract_title
import unittest

class TestTitle(unittest.TestCase):
    def test_extract_title(self):
        text = "#    This is a Header    "
        result = extract_title(text)
        expected = "This is a Header"
        self.assertEqual(result, expected)

    def test_not_header(self):
        text = "    This is not a Header    "
        with self.assertRaises(Exception):
            extract_title(text)