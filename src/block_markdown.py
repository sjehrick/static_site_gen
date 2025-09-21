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
    match block:
        case block.startswith("#"):
            return BlockType.HEADING
        case block.startswith("```") and block.endswith("```"):
            return BlockType.CODE
        #should I use the match case syntax here or just go for a bunch of if statements?
        #for quote, split the block into line with a \n delimiter then use startswith
        #for UL same as quote but starts with is "- "
        #for OL might have to see if startswith supports pattern matching or use for loop
        #none is the default condition 
