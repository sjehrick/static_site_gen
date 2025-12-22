#from htmlnode import HTMLNode
#from textnode import *
from copy_source_dest import copy_source_dest
from generatepage import *

def main():
    copy_source_dest("static", "public")

    generate_pages_recursive("content", "template.html", "public")

main()
