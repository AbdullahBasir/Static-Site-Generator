from copystatic import static_to_public
import os
from bulk_page_generation import generate_pages_recursive

project_dir = os.getcwd()
static_path = os.path.join(project_dir, "static")
public_path = os.path.join(project_dir, "public")
content_path = os.path.join(project_dir, "content")
template_path = os.path.join(project_dir, "template.html")

def main():

    static_to_public(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path)

if __name__ == "__main__":
    main()