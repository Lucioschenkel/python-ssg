import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "The text")
        html_props = node.props_to_html()
        self.assertEqual(html_props, "")

        node = HTMLNode("a", "This link", None, {
            "href": "http://localhost",
            "target": "_blank"
        })
        html_props = node.props_to_html()
        self.assertEqual(html_props, " href=\"http://localhost\" target=\"_blank\"")

    def test_repr(self):
        node = HTMLNode("p", "The text")
        self.assertEqual(str(node), "HTMLNode(p, The text, None, None)")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Google", {
            "href": "https://google.com",
            "target": "_blank"
        })
        self.assertEqual(node.to_html(), "<a href=\"https://google.com\" target=\"_blank\">Google</a>")


if __name__ == "__main__":
    unittest.main()
