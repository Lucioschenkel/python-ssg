from fs import cleanup_directory, copy_recursive, create_directory
from generate_page import generate_pages_recursive


def main():
    # Cleanup public directory
    cleanup_directory("public")

    # Re-create an empty public directory
    create_directory("public")

    # Recursively copy files from "static" to "public"
    copy_recursive("static", "public")

    # Generate HTML from Markdown
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
