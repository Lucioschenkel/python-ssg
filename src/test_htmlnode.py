import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props_and_children(self):
        children = [
            LeafNode("p", "child 1"),
            LeafNode("a", "child 2")
        ]
        parent_node = ParentNode("div", children, {
            "contenteditable": "true"
        })
        self.assertEqual(
            parent_node.to_html(),
            "<div contenteditable=\"true\"><p>child 1</p><a>child 2</a></div>"
        )

if __name__ == "__main__":
    unittest.main()
