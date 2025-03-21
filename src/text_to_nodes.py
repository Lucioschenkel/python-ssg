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
    # Start with a single node
    nodes = [TextNode(text, TextType.TEXT)]

    # Define a list of transformation functions
    transformations = [
        (split_nodes_link, None, None),
        (split_nodes_image, None, None),
        (split_nodes_delimiter, "`", TextType.CODE),
        (split_nodes_delimiter, "**", TextType.BOLD),
        (split_nodes_delimiter, "_", TextType.ITALIC),
    ]
    # Loop through transformation functions and apply them to the node lists
    for transform_func, delimiter, text_type in transformations:
        if delimiter and text_type:
            nodes = transform_func(nodes, delimiter, text_type)
        else:
            nodes = transform_func(nodes)

    return nodes
