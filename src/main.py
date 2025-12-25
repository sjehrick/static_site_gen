import sys
from copy_source_dest import copy_source_dest
from generatepage import *

def main():
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_source_dest("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
