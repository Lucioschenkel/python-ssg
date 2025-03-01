import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a link node", TextType.LINK, "https://something.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        repr = str(node)
        self.assertEqual(repr, "TextNode(This is a text node, normal, None)")


if __name__ == "__main__":
    unittest.main()
