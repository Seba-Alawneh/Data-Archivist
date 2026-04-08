import sys


def main() -> None:
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file = open(sys.argv[1], 'r')
        print(file.read())
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
