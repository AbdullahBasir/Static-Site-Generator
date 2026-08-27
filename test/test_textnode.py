import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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

    #text_node_to_html_node function tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

if __name__ == "__main__":
    unittest.main()