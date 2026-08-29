def extract_title(markdown: str) -> str:
    header = markdown.split("\n")[0]
    hashed, stripped = header.split(" ", 1)
    if hashed != "#":
        raise Exception("header is missing")
    return stripped.strip()