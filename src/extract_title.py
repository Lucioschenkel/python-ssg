def extract_title(md: str) -> str:
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.replace("#", "").strip()

    raise Exception("no title found in document")
