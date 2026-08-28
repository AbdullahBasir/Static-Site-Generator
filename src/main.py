from copystatic import static_to_public
import os

def main():

    project_dir = os.getcwd()
    source_path = os.path.join(project_dir, "static")
    dest_path = os.path.join(project_dir, "public")
    static_to_public(source_path, dest_path)

if __name__ == "__main__":
    main()