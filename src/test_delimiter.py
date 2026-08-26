import unittest
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_italic(self):
        node = TextNode("This is _italic_ text", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_code(self):
        node = TextNode("This is `code` text", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(result, expected)