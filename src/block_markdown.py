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

def block_to_block_type(block):
    if block.startswith("#"):
       return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
       return BlockType.CODE
    if block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                raise Exception("Error: not a valid MD quote block")
        return BlockType.QUOTE
    if block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith("- "):
                raise Exception("Error: not a valid MD unordered list")
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        lines = block.split("\n")
        for i in range(len(lines)):
             
                raise Exception("Error: not a valid MD ordered list")
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

        #for quote, split the block into line with a \n delimiter then use startswith
        #for UL same as quote but starts with is "- "
        #for OL might have to see if startswith supports pattern matching or use for loop
        #none is the default condition 
