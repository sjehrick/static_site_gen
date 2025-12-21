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

    to_html_from_markdown = html_from_markdown.to_html()

    markdown_title = extract_title(markdown_content)

    html_template_wtitle = html_content.replace("{{ Title }}", markdown_title)

    complete_html_template = html_template_wtitle.replace("{{ Content }}", to_html_from_markdown)

    dir_path = os.path.dirname(dest_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(dest_path, "w") as file:
        file.write(complete_html_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}")
