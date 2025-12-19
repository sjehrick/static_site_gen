#from htmlnode import HTMLNode
#from textnode import *
from copy_source_dest import copy_source_dest
from generatepage import generate_page

def main():
    copy_source_dest("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")

main()
