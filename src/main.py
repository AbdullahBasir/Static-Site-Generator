from copystatic import static_to_public
from bulk_page_generation import generate_pages_recursive
import sys
import os


base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
project_dir = os.getcwd()
static_path = os.path.join(project_dir, "static")
docs_path = os.path.join(project_dir, "docs")
content_path = os.path.join(project_dir, "content")
template_path = os.path.join(project_dir, "template.html")

def main():

    static_to_public(static_path, docs_path)
    generate_pages_recursive(content_path, template_path, docs_path, base_path)

if __name__ == "__main__":
    main()