import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode('p', 'i am a node', None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })

        as_text = node.props_to_html()

        self.assertEqual(
            as_text, ' href="https://www.google.com" target="_blank"')

    def test_vals(self):
        node = HTMLNode('div', 'hello world')

        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'hello world')

    def test_repr(self):
        node = HTMLNode('p', 'Witam konsumenta', None, {'href': '_blank'})

        self.assertEqual(node.__repr__(
        ), "HTMLNode(p, Witam konsumenta, children: None, {'href': '_blank'})")
