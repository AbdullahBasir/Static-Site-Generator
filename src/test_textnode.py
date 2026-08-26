import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a url link", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a url link", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_url_default_none(self):
        node = TextNode("Boot.dev", TextType.PLAIN_TEXT)
        self.assertIsNone(node.url)
        
if __name__ == "__main__":
    unittest.main()