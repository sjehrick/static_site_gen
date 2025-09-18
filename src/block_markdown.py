from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    new_blocks = []

    working_blocks = markdown.split("\n\n")

    for block in working_blocks:    
        if block == "":
            continue
        block = block.strip()
        new_blocks.append(block)

    return new_blocks
