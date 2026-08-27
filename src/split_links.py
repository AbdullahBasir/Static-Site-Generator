from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old)
            continue
        if not old.text:
            continue

        current_text = old.text
        images = extract_markdown_images(current_text)

        if not images:
            new_nodes.append(TextNode(current_text, TextType.PLAIN_TEXT))
            continue

        for image_alt, image_link in images:
            before, current_text = current_text.split(f"![{image_alt}]({image_link})", 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.PLAIN_TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old)
            continue

        if not old.text:
            continue

        current_text = old.text
        url = extract_markdown_links(current_text)

        if not url:
            new_nodes.append(TextNode(current_text, TextType.PLAIN_TEXT))
            continue

        for url_alt, url_link in url:
            before, current_text = current_text.split(f"[{url_alt}]({url_link})", 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(url_alt, TextType.LINK, url_link))

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.PLAIN_TEXT))

    return new_nodes
        

