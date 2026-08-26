from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old)
            continue

        parts = old.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax: unmatched delimiter '{delimiter}'")

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.PLAIN_TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes
        