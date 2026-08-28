from htmlnode import HTMLNode, ParentNode
from children import text_to_children
from split_blocks import markdown_to_blocks
from block_type import block_to_block_type, BlockType
from textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    outer_div = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                cleaned_block = block.replace("\n", " ")
                outer_div.append(ParentNode(tag="p", children=text_to_children(cleaned_block)))

            case BlockType.HEADING:
                length_hash, stripped = block.split(" ", 1)
                outer_div.append(ParentNode(tag=f"h{len(length_hash)}", children=text_to_children(stripped)))

            case BlockType.CODE:
                text = block.lstrip("`\n").rstrip("`")
                text_node = TextNode(text, TextType.PLAIN_TEXT)
                code_node = ParentNode(tag="code", children=[text_node_to_html_node(text_node)])
                outer_div.append(ParentNode(tag="pre", children=[code_node]))

            case BlockType.QUOTE:
                text = []
                for line in block.split("\n"):
                    text.append(line.strip(">"))
                stripped = "\n".join(text)
                outer_div.append(ParentNode(tag="blockquote", children=text_to_children(stripped)))

            case BlockType.UNORDERED_LIST:
                result = []
                for line in block.split("\n"):
                    _, stripped = line.split(" ", 1)
                    result.append(ParentNode(tag="li", children=text_to_children(stripped)))
                outer_div.append(ParentNode(tag="ul", children=result))

            case BlockType.ORDERED_LIST:
                result = []
                split_block = block.split("\n")
                for i, line in enumerate(split_block):
                    prefix = f"{i + 1}. "
                    stripped = line[len(prefix):] 
                    result.append(ParentNode(tag="li", children=text_to_children(stripped)))
                outer_div.append(ParentNode(tag="ol", children=result))

    return ParentNode(tag="div", children=outer_div)
