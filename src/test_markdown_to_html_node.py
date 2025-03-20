import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
- this
- is
- a **list**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, "<div><ul><li>this</li><li>is</li><li>a <b>list</b></li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. this
2. is
3. a list
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, "<div><ol><li>this</li><li>is</li><li>a list</li></ol></div>"
        )

    def test_blockquote(self):
        md = """
> this
> is a
> **blockquote**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, "<div><blockquote>this is a <b>blockquote</b></blockquote></div>"
        )
