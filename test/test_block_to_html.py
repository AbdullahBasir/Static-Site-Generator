import unittest
from markdown_to_html import markdown_to_html_node

class TestBlockToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(result, expected)


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        self.assertEqual(result, expected)

    def test_heading(self):
        md = "### A heading with **bold** text"
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><h3>A heading with <b>bold</b> text</h3></div>"
        self.assertEqual(result, expected)

    def test_quote(self):
        md = ">First quoted line\n> Second quoted line"
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><blockquote>First quoted line\nSecond quoted line</blockquote></div>"
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        md = "- First item\n- Second item with _italic_ text"
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><ul><li>First item</li><li>Second item with <i>italic</i> text</li></ul></div>"
        self.assertEqual(result, expected)

    def test_ordered_list(self):
        md = "1. First item\n2. Second item with `code`"
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><ol><li>First item</li><li>Second item with <code>code</code></li></ol></div>"
        self.assertEqual(result, expected)