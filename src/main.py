import sys

from fs import cleanup_directory, copy_recursive, create_directory
from generate_page import generate_pages_recursive


def main():
    # Cleanup public directory
    cleanup_directory("docs")

    # Re-create an empty public directory
    create_directory("docs")

    # Recursively copy files from "static" to "public"
    copy_recursive("static", "docs")

    # Generate HTML from Markdown
    # generate_page("content/index.md", "template.html", "public/index.html")
    basepath = "/" if len(sys.argv) <= 1 else sys.argv[1]
    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="docs",
        basepath=basepath,
    )


if __name__ == "__main__":
    main()
