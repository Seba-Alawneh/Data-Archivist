import sys


def cat() -> None:
    file = open(sys.argv[1], 'r')
    sys.stdout.write(file.read() + "\n")
    file.close()


def Modification() -> str:
    file = open(sys.argv[1], 'r')
    content = file.read()
    file.close()
    if content:
        content = content.replace('\n', '#\n')
        if content[-1] != "\n":
            content += "#"
    return content


def save_new_content(new_content: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    for line in sys.stdin:
        file_name = line.strip()
        if file_name == "":
            print("Not saving data.")
            return
        try:
            print(f"Saving data to '{file_name}'")
            new_file = open(file_name, "w")
            new_file.write(new_content)
            new_file.close()
            sys.stdout.write(f"Data saved in file '{file_name}'.\n")
            return
        except (FileNotFoundError, PermissionError) as e:
            sys.stderr.write("\n[STDERR]Error opening file ")
            sys.stderr.write(f"'{file_name}': {e}\n")
            sys.stdout.write("Data not saved.\n")
            return


def main() -> None:
    if len(sys.argv) <= 1:
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>\n")
        return
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{sys.argv[1]}'\n")
    try:
        cat()
        sys.stdout.write(f"\nFile '{sys.argv[1]}' closed.\n")
        sys.stdout.write("Transform data:\n")
        new_content = Modification()
        sys.stdout.write(new_content + "\n")
        save_new_content(new_content)
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR]Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
