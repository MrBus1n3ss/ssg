from htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self, tag, value, children, props):
        if children is None:
            super().__init__(tag, value, children, props)
        else:
            raise ValueError()

    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
