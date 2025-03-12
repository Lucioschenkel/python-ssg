import re
from typing import List, Callable, Tuple

from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.IMAGE:
            return LeafNode("img", "", {
                "src": text_node.url,
                "alt": text_node.text
            })
        case TextType.LINK:
            return LeafNode("a", text_node.text, {
                "href": text_node.url
            })

    raise ValueError('Invalid text_node type')

def make_node_delimiter_processor(old_node: TextNode, new_text_type: TextType) -> Callable[[TextNode], TextNode]:
    def node_delimiter_processor(element: Tuple[int, str]) -> TextNode:
        index, text = element
        # Odd indexes are where the matches for a given text block are
        text_type = new_text_type if index % 2 != 0 else old_node.text_type
        return TextNode(text, text_type, old_node.url)

    return node_delimiter_processor

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_nodes = node.text.split(delimiter)
        node_delimiter_processor = make_node_delimiter_processor(node, text_type)
        nodes_to_add = filter(lambda n: len(n.text) > 0, list(map(node_delimiter_processor, enumerate(split_nodes))))
        new_nodes.extend(nodes_to_add)

    return new_nodes

def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes(nodes: List[TextNode], extract_node_func: Callable[[str], List[Tuple[str, str]]], text_type: TextType) -> List[TextNode]:
    new_nodes = []
    for node in nodes:
        # Either a link or an image
        external_refs = extract_node_func(node.text)
        node_text = node.text
        for alt, url in external_refs:
            delimiter = f"![{alt}]({url})" if text_type == TextType.IMAGE else f"[{alt}]({url})"
            [text_node_before, *after] = node_text.split(delimiter)
            node_text = "".join(after)
            new_nodes.extend([TextNode(text_node_before, node.text_type, node.url), TextNode(alt, TextType.IMAGE, url)])

        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, node.text_type, node.url))

    return new_nodes


def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    return split_nodes(old_nodes, extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    return split_nodes(old_nodes, extract_markdown_links, TextType.LINK)

