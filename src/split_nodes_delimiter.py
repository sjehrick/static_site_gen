from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        working_node_text = []
        sections = node.text.split(delimiter)
        
        if len(sections) % 2 == 0:
            raise ValueError(f"Error: matching closing delimiter not found. Did you forget to add a {delimiter} in your markdown?")
            
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                working_node_text.append(TextNode(sections[i], TextType.TEXT))
            else:
                working_node_text.append(TextNode(sections[i], text_type))
        new_nodes.extend(working_node_text)
    return new_nodes
