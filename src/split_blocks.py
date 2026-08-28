def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        stripped_block = block.lstrip("\n ").rstrip(" \n")
        if block == "":
            continue
        filtered.append(stripped_block)
    return filtered