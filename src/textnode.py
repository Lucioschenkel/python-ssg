from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    IMAGE = "image"
    LINK = "link"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        text_is_equal = self.text == target.text
        text_type_is_equal = self.text_type == target.text_type
        url_is_equal = self.url == target.url

        return text_is_equal and text_is_equal and url_is_equal

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
