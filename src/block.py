import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_unordered_list(block: str) -> bool:
    lines = block.split("\n")
    return all(line.startswith("- ") for line in lines)

def is_ordered_list(block: str) -> bool:
    lines = block.split("\n")
    return all(re.match(r"^\d+\.(.*)$", line) for line in lines)

def is_quote(block: str) -> bool:
    lines = block.split("\n")
    return all(line.startswith("> ") for line in lines)

def is_heading(block: str) -> bool:
    return re.match(r"^#+ ", block)

def is_code(block: str) -> bool:
    return block.startswith("```") and block.endswith("```")

def block_to_block_type(block: str) -> BlockType:
    match_functions = [
        (is_unordered_list, BlockType.UNORDERED_LIST),
        (is_ordered_list, BlockType.ORDERED_LIST),
        (is_quote, BlockType.QUOTE),
        (is_code, BlockType.CODE),
        (is_heading, BlockType.HEADING),
    ]

    for check_function, return_type in match_functions:
        if check_function(block.strip()):
            return return_type

    return BlockType.PARAGRAPH

