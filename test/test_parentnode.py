import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_values(self):
        child_node = LeafNode("span", "child")
        node = ParentNode("a", child_node)
        self.assertIsNone(node.props)
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.children, child_node)

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)

    def test_raises(self):
        node = ParentNode("p", None)
        child_node = LeafNode("span", "child")
        node2 = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            node.to_html()
            node2.to_html()

if __name__ == "__main__":
    unittest.main()