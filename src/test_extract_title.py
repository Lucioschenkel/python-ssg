import unittest

from extract_title import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Title
## Subtitle
My content
"""
        title = extract_title(md)
        self.assertEqual(title, "Title")

        md = """
This is some text
# Before the title
"""
        title = extract_title(md)
        self.assertEqual(title, "Before the title")
