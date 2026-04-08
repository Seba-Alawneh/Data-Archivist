import sys


def cat() -> None:
    file = open(sys.argv[1], 'r')
    print(file.read())
    file.close()


def Modification() -> str:
    file = open(sys.argv[1], 'r')
    content = file.read()
    file.close()
    if content:
        content = content.replace('\n', '#\n')
        if content[-1] != "\n" and content[-1] != "#":
            content += "#"
    return content


def save_new_content(new_content: str) -> None:
    name_new_file = input("Enter new file name (or empty): ")
    if name_new_file == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{name_new_file}'")
        new_file = open(name_new_file, "w")
        new_file.write(new_content)
        new_file.close()
        print(f"Data saved in file '{name_new_file}'.")


def main() -> None:
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        cat()
        print(f"\nFile '{sys.argv[1]}' closed.")
        print("Transform data:")
        new_content = Modification()
        print(new_content)
        save_new_content(new_content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
