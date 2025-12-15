def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            new_line = line.strip("# ")
            return new_line

    raise Exception("No h1 heading found")
