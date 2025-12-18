import os
from extractmdtitle import extract_title
from block_markdown import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = ""
    with open(from_path, "r") as file:
        markdown_content = file.read()

    html_content = ""
    with open(template_path, "r") as file:
        html_content = file.read()

    html_from_markdown = markdown_to_html_node(markdown_content)

    markdown_title = extract_title(markdown_content)

    html_template_wtitle = html_content.replace("{{ Title }}", markdown_title)

    complete_html_template = html_template_wtitle.replace("{{ Content }}", html_from_markdown)

    dir_path = os.path.dirname(dest_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(dest_path, "w") as file:
        file.write(complete_html_template)
