import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Open both files in a with block to make sure they're properly closed
    with (
        open(from_path, "r", encoding="utf-8") as markdown_file,
        open(template_path, "r", encoding="utf-8") as template_file,
    ):
        template = template_file.read()
        md = markdown_file.read()

        print(template)

        # Generate HTML from markdown
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()

        # Extract the title from an H1 in markdown, i.e a line that starts with '# '
        title = extract_title(md)

        # Replace the placeholders in the template with the tile and content
        rendered = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

        # Create the destination directory if it doesn't exists
        destination_directory = os.path.dirname(dest_path)
        if not os.path.exists(destination_directory):
            os.mkdir(destination_directory)

        # Write the rendered output to the destination file
        with open(dest_path, "w", encoding="utf-8") as destination_file:
            destination_file.write(rendered)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
):
    files = os.listdir(dir_path_content)

    for file in files:
        file_path = os.path.join(dir_path_content, file)
        if os.path.isfile(file_path):
            full_destination_path = os.path.join(
                dest_dir_path, file.replace(".md", ".html")
            )
            generate_page(file_path, template_path, full_destination_path)
        else:
            generate_pages_recursive(
                file_path, template_path, os.path.join(dest_dir_path, file)
            )
