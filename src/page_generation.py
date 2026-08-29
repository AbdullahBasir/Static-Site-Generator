from markdown_to_html import markdown_to_html_node
from title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    content_file = os.path.join(from_path, "index.md")
    with open(file=content_file) as f:
        read_from_md = f.read()

    with open(file=template_path) as t:
        read_temp = t.read()

    node = markdown_to_html_node(read_from_md)
    html_content = node.to_html()
    html_title = extract_title(read_from_md)

    read_temp = read_temp.replace("{{ Title }}", html_title)
    read_temp = read_temp.replace("{{ Content }}", html_content)

    os.makedirs(dest_path, exist_ok=True)

    dest_file = os.path.join(dest_path, "index.html")
    with open(file=dest_file, mode="w") as d:
        d.write(read_temp)
