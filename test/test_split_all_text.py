import unittest
from textnode import TextNode, TextType
from split_all_text import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_no_text_type(self):
        text = "Just plain text, no fonts or links here."
        result = text_to_textnodes(text)
        expected = [TextNode("Just plain text, no fonts or links here.", TextType.PLAIN_TEXT)]
        self.assertEqual(result, expected)

    def test_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.PLAIN_TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

    def test_wrong_text_type(self):
        text = "This is not an **italic** word"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is not an ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word", TextType.PLAIN_TEXT),
        ]
        self.assertNotEqual(result, expected)

