import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_blank"')

    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "text"})
        expected = "HTMLNode(p, Hello, None, {'class': 'text'})"
        self.assertEqual(repr(node), expected)

    def test_values_default_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

if __name__ == "__main__":
    unittest.main()