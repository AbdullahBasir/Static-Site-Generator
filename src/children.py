from textnode import text_node_to_html_node
from htmlnode import LeafNode
from split_all_text import text_to_textnodes

def text_to_children(text) -> list["LeafNode"]:
    result = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        result.append(text_node_to_html_node(node))
    return result
