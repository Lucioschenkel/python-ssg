from typing import List

def markdown_to_blocks(text: str) -> List[str]:
    return list(filter(len, map(str.strip, text.split("\n\n"))))
