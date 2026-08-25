import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_repr(self):
        node = LeafNode("p", "Hello", {"class": "text"})
        expected = "LeafNode(p, Hello, {'class': 'text'})"
        self.assertEqual(repr(node), expected)

    def test_values(self):
        node = LeafNode("a", "click me")
        self.assertIsNone(node.props)
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "click me")