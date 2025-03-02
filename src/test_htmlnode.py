import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
