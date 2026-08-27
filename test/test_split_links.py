import unittest
from textnode import TextNode, TextType
from split_links import split_nodes_image, split_nodes_link

class TestSplitNodesImage(unittest.TestCase):
    def test_no_images(self):
        node = TextNode("Just plain text, no images here.", TextType.PLAIN_TEXT)
        result = split_nodes_image([node])
        expected = [TextNode("Just plain text, no images here.", TextType.PLAIN_TEXT)]
        self.assertEqual(result, expected)

    def test_single_image(self):
        node = TextNode("![alt](url)", TextType.PLAIN_TEXT)
        result = split_nodes_image([node])
        expected = [TextNode("alt", TextType.IMAGE, "url")]
        self.assertEqual(result, expected)

    def test_image_with_trailing_text(self):
        node = TextNode("![alt](url) trailing text", TextType.PLAIN_TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("alt", TextType.IMAGE, "url"),
            TextNode(" trailing text", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        result = split_nodes_image([node])
        expected =[
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN_TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(result, expected)

class TestSplitNodesLink(unittest.TestCase):
    def test_no_link(self):
        node = TextNode("Just plain text, no links here.", TextType.PLAIN_TEXT)
        result = split_nodes_link([node])
        expected = [TextNode("Just plain text, no links here.", TextType.PLAIN_TEXT)]
        self.assertEqual(result, expected)

    def test_single_link(self):
        node = TextNode("[alt](url)", TextType.PLAIN_TEXT)
        result = split_nodes_link([node])
        expected = [TextNode("alt", TextType.LINK, "url")]
        self.assertEqual(result, expected)

    def test_link_with_trailing_text(self):
        node = TextNode("[alt](url) trailing text", TextType.PLAIN_TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("alt", TextType.LINK, "url"),
            TextNode(" trailing text", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_links(self):
        node = TextNode(
            "This is text with an [url](https://boot.dev) and another [second url](https://github.com)",
            TextType.PLAIN_TEXT,
        )
        result = split_nodes_link([node])
        expected =[
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("url", TextType.LINK, "https://boot.dev"),
            TextNode(" and another ", TextType.PLAIN_TEXT),
            TextNode("second url", TextType.LINK, "https://github.com"),
        ]
        self.assertEqual(result, expected)