from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

    for node in old_nodes:
        if node.text_type == TextType.Text:
            if node.text.count(delimiter) % 2 != 0:
                raise ValueError("Error: matching closing delimiter not found. Did you forget to add a {delimiter} in your markdown?")
