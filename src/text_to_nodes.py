from typing import List

from textnode import TextNode, TextType
from utils import split_nodes_image, split_nodes_delimiter, split_nodes_link

def text_to_nodes(text: str) -> List[TextNode]:
    """
    Convert a single line of markdown formatted string to a list of markdown nodes.

    Supported nodes:
    1. Text
    2. Italic
    3. Bold
    4. Inline Code
    4. Image
    5. Link
    """
    nodes = []
    initial_node = TextNode(text, TextType.TEXT)
    with_images = split_nodes_image([initial_node])
    with_links = split_nodes_link(with_images)
    with_code = split_nodes_delimiter(with_links, "`", TextType.CODE)
    with_bold = split_nodes_delimiter(with_code, "**", TextType.BOLD)
    with_italic = split_nodes_delimiter(with_bold, "_", TextType.ITALIC)
    return with_italic
