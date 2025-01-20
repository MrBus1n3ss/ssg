import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_check_props_to_html_eq(self):
        node = HTMLNode("h1", "some text", props={'href': 'http://www.google.com', 'target': '_blank',})
        self.assertEqual(node.props_to_html(), ' href=http://www.google.com target=_blank')

    def test_check_props_to_html_not_eq(self):
        node = HTMLNode("h1", "some text", props={'href': 'http://www.google.com', 'target': '_blank',})
        self.assertNotEqual(node.props_to_html(), 'href=http://www.google.com target=_blank')

    def test_check_props_to_html_none(self):
        node = HTMLNode("h1", "some text")
        try:
            node.props_to_html()
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print(e)
