import unittest

from utils import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode

class TestUtilsTextNodeToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def text_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")

class TestUtilsSplitNodesDelimiter(unittest.TestCase):
    def test_single_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_multiple_nodes(self):
        old_nodes = [
            TextNode("node 1 `code`", TextType.TEXT),
            TextNode("`code` node 2", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertListEqual(new_nodes, [
            TextNode("node 1 ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("code", TextType.CODE),
            TextNode(" node 2", TextType.TEXT),
        ])

class TestUtilsExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        matches = extract_markdown_images(
            "This another text ![image](http://localhost.com) also ![another](http://localhost.dev)"
        )
        self.assertEqual([("image", "http://localhost.com"), ("another", "http://localhost.dev")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "[this is a link](http://localhost.dev)"
        )
        self.assertListEqual([("this is a link", "http://localhost.dev")], matches)


if __name__ == "__main__":
    unittest.main()
