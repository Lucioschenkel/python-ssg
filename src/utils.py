import re

from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_nodes = node.text.split(delimiter)
        nodes_to_add = filter(
            lambda n: len(n.text) > 0,
            list(
                map(lambda e: TextNode(e[1], text_type) if e[0] % 2 != 0 else TextNode(e[1], node.text_type, node.url), enumerate(split_nodes))
            )
        )
        new_nodes.extend(nodes_to_add)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        node_text = node.text
        for image in images:
            alt, url = image
            [text_node_before, *after] = node_text.split(f"![{alt}]({url})")
            node_text = "".join(after)
            new_nodes.extend([TextNode(text_node_before, node.text_type, node.url), TextNode(alt, TextType.IMAGE, url)])

        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, node.text_type, node.url))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        node_text = node.text
        for link in links:
            alt, url = link
            [text_node_before, *after] = node_text.split(f"[{alt}]({url})")
            node_text = "".join(after)
            new_nodes.extend([TextNode(text_node_before, node.text_type, node.url), TextNode(alt, TextType.LINK, url)])

        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, node.text_type, node.url))

    return new_nodes
