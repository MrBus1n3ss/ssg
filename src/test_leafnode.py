import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_create_with_children(self):
        try:
            LeafNode("h1", "some text", ["div"], {"href": "http://www.google.com", "target": "_blank", })
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print(e)

    def test_create_without_children(self):
        node = LeafNode("h1", "some text", None, {"href": "http://www.google.com", "target": "_blank", })
        self.assertTrue(isinstance(node, LeafNode))

    def test_to_html_with_value_and_tag(self):
        node = LeafNode("h1", "some text", None, {"href": "http://www.google.com", "target": "_blank", })
        self.assertEqual('<h1 href=http://www.google.com target=_blank>some text</h1>', node.to_html())

    def test_to_html_with_value_without_tag(self):
        node = LeafNode(None, "some text", None, {"href": "http://www.google.com", "target": "_blank", })
        self.assertEqual('some text', node.to_html())

    def test_to_html_without_value(self):
        node = LeafNode("h1", None, None, {"href": "http://www.google.com", "target": "_blank", })
        try:
            node.to_html()
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
