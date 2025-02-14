import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_texttype_not_eq(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT, "https://superawesome.io")
        self.assertNotEqual(node, node2)

    def test_type_eq(self):
        node = TextNode("This is a node", TextType.ITALIC)
        node2 = TextNode("This is a node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a node", TextType.LINK, "https://codingisfun.com")
        node2 = TextNode("This is a node", TextType.LINK, "https://codingisfun.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()