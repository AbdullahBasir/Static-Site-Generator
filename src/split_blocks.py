def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        if block == "":
            continue
        stripped_block = block.strip()
        filtered.append(stripped_block)
    return filtered