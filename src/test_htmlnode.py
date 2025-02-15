import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_node_eq(self):
        node = HTMLNode("a", "this is a test htmlnode", None, {"href": "https://www.test.com", "target": "_blank"})
        node2 = HTMLNode("a", "this is a test htmlnode", None, {"href": "https://www.test.com", "target": "_blank"})
        self.assertEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()