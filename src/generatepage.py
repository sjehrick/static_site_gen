import os
import shutil
from extractmdtitle import extract_title
from block_markdown import *

def generate_page(from_path, template_path, dest_path, basepath):
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

    html_template_title = html_content.replace("{{ Title }}", markdown_title)

    html_template_content = html_template_title.replace("{{ Content }}", to_html_from_markdown)

    html_basepath_href = html_template_content.replace('href="/', 'href="' + basepath)

    complete_html_template = html_basepath_href.replace('src="/', 'src="' + basepath)

    dir_path = os.path.dirname(dest_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(dest_path, "w") as file:
        file.write(complete_html_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print(f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}")

    files = [file for file in os.listdir(dir_path_content) if os.path.isfile(os.path.join(dir_path_content, file))]

    nested_dirs = [dir for dir in os.listdir(dir_path_content) if os.path.isdir(os.path.join(dir_path_content, dir))]

    for file in files:
        if file.endswith(".md"):
            full_path = os.path.join(dir_path_content, file)
            dest_file_name = os.path.join(dest_dir_path, "index.html")
            print(f"Creating page using {full_path}. Writing to {dest_dir_path}")
            generate_page(full_path, template_path, dest_file_name, basepath)

    for dir in nested_dirs:
        new_source = os.path.join(dir_path_content, dir)
        new_dest = os.path.join(dest_dir_path, dir)

        shutil.rmtree(new_dest, ignore_errors=True)

        os.mkdir(new_dest)

        if os.path.exists(new_dest):
            print(f"{new_dest} successfully created")

        generate_pages_recursive(new_source, template_path, new_dest, basepath)
