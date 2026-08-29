from copystatic import static_to_public
import os
from page_generation import generate_page

def main():

    project_dir = os.getcwd()
    static_path = os.path.join(project_dir, "static")
    public_path = os.path.join(project_dir, "public")
    static_to_public(static_path, public_path)

    content_path = os.path.join(project_dir, "content")
    template_path = os.path.join(project_dir, "template.html")
    generate_page(content_path, template_path, public_path)

if __name__ == "__main__":
    main()