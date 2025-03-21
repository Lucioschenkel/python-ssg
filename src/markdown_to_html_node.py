import re
from htmlnode import ParentNode, LeafNode
from utils import text_node_to_html_node
from markdown_to_blocks import markdown_to_blocks
from block import block_to_block_type, BlockType
from text_to_nodes import text_to_nodes


def block_type_to_html_tag(block_type: BlockType) -> str:
    match block_type:
        case BlockType.HEADING:
            return "h1"
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case BlockType.CODE:
            return "code"
        case BlockType.QUOTE:
            return "blockquote"


def create_code_block_from_md(block: str, tag: str) -> ParentNode:
    code = block.replace("```", "").strip()
    code_node = LeafNode(tag, code + "\n")
    pre_node = ParentNode("pre", [code_node])
    return pre_node


def create_unordered_list_from_md(block: str, tag: str) -> ParentNode:
    items = list(map(lambda i: i.replace("- ", "", count=1), block.split("\n")))
    li_nodes = []
    for li in items:
        li_text_children = text_to_nodes(li.replace("- ", "", count=1))
        li_children = [text_node_to_html_node(node) for node in li_text_children]
        li_node = ParentNode("li", li_children)
        li_nodes.append(li_node)

    return ParentNode(tag, li_nodes)


def create_ordered_list_from_md(block: str, tag: str) -> ParentNode:
    items = list(
        map(lambda item: re.sub(r"^\d+\. ", "", item, count=1), block.split("\n"))
    )
    li_nodes = []
    for li in items:
        li_text_children = text_to_nodes(li)
        li_children = [text_node_to_html_node(node) for node in li_text_children]
        li_node = ParentNode("li", li_children)
        li_nodes.append(li_node)

    return ParentNode(tag, li_nodes)


def create_blockquote_from_md(block: str, tag: str) -> ParentNode:
    quote_text = block.replace("\n", "").replace(">", "").strip(" ")
    print(quote_text)
    quote_nodes = []
    text_nodes = text_to_nodes(quote_text)
    children = [text_node_to_html_node(node) for node in text_nodes]
    quote_nodes.extend(children)

    return ParentNode(tag, quote_nodes)


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        parent_tag = block_type_to_html_tag(block_type)
        match block_type:
            case BlockType.CODE:
                nodes.append(create_code_block_from_md(block, parent_tag))
                continue
            case BlockType.UNORDERED_LIST:
                nodes.append(create_unordered_list_from_md(block, parent_tag))
                continue
            case BlockType.ORDERED_LIST:
                nodes.append(create_ordered_list_from_md(block, parent_tag))
                continue
            case BlockType.QUOTE:
                nodes.append(create_blockquote_from_md(block, parent_tag))
                continue

        text_nodes = text_to_nodes(block)
        children = [text_node_to_html_node(node) for node in text_nodes]
        parent = ParentNode(parent_tag, children)
        nodes.append(parent)

    html_root = ParentNode("div", nodes)
    return html_root
