import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestLeafNode(unittest.TestCase):

    def test_empty_value(self):
        node = LeafNode('p', None)

        self.assertRaises(ValueError, node.to_html)

    def test_empty_tag(self):
        node = LeafNode(None, "text").to_html()

        self.assertEqual(node, "text")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
