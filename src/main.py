from fs import cleanup_directory, copy_recursive, create_directory


def main():
    # Cleanup public directory
    cleanup_directory("public")

    # Re-create an empty public directory
    create_directory("public")

    # Recursively copy files from "static" to "public"
    copy_recursive("static", "public")


if __name__ == "__main__":
    main()
