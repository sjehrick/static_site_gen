def markdown_to_blocks(markdown):
    new_blocks = []

    working_blocks = markdown.split("\n\n")

    for block in working_blocks:    
        if block == "":
            continue
        block = block.strip()
        new_blocks.append(block)

    return new_blocks
