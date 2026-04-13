def secure_archive(file_name, action="r", content="") -> tuple:
    try:
        if action != "r" or action != "w":
            return
        if action == "r":
            with open(file_name, "r") as file:
                return (True, file.read())
        if action == "w":
            with open(file_name, "w") as file:
                file.write(content + "\n")
                return (True, "Content successfully written to file")
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("notper", "r"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("myfile", "r"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("content", "w", "Some new content here"))


if __name__ == "__main__":
    main()
