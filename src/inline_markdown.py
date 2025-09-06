import re

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
            raise ValueError(
                f"Error: matching closing delimiter not found. Did you forget to add a {
                    delimiter} in your markdown?"
            )

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                working_node_text.append(TextNode(sections[i], TextType.TEXT))
            else:
                working_node_text.append(TextNode(sections[i], text_type))
        new_nodes.extend(working_node_text)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        image_extractions = extract_markdown_images(node.text)

        if len(image_extractions) == 0:
            return [old_nodes]
        #this should probably be inside another loop so each extracted link in the array is processed.
        image_alt = image_extractions[0][0]
        image_link = image_extractions[0][1]
    
        working_node_text = []
        sections = node.text.split(f"!{image_alt}]({image_link})", 1)


def split_nodes_link(old_nodes):
