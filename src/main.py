from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.win.com")
    html_node = HTMLNode("a", "this is a test htmlnode", None, {"href": "https://www.test.com", "target": "_blank"})

    print(text_node)
    print(html_node.props_to_html())



main()