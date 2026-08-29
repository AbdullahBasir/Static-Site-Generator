from markdown_to_html import markdown_to_html_node
from title import extract_title
from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    content_path = Path(dir_path_content)
    dest_path = Path(dest_dir_path)
    template_path = Path(template_path)

    for item in content_path.iterdir():
        if item.is_file() and item.suffix == ".md":
            md_content = item.read_text()
            template_content = template_path.read_text()
            
            node = markdown_to_html_node(md_content)
            html_content = node.to_html()
            html_title = extract_title(md_content)
            
            template_content = template_content.replace("{{ Title }}", html_title)
            template_content = template_content.replace("{{ Content }}", html_content)
            template_content = template_content.replace('href="/', f'href="{base_path}')
            template_content = template_content.replace('src="/', f'src="{base_path}')

            output_file = dest_path / item.relative_to(content_path).with_suffix(".html")
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(template_content)

        elif item.is_dir():
            generate_pages_recursive(item, template_path, dest_path / item.name, base_path)