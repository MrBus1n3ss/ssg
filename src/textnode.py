from enum import Enum


class TextType(Enum):
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS_TEXT = "links"
    IMAGES_TEXT = "images"


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        if isinstance(text_node, TextNode):
            if text_node.text == self.text and text_node.text_type == self.text_type and text_node.url == self.url:
                return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
