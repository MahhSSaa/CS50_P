import sys
import os

def main():
    # Check if the user provided exactly one command-line argument
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    # Check if the file has a .py extension
    if not file_path.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File does not exist")
        sys.exit(1)

    # Count the lines of code in the file
    loc = count_lines_of_code(file_path)
    # Print the number of lines of code
    print(f"Number of lines of code: {loc}")


def count_lines_of_code(file_path):
    loc = 0
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            for line in file:
                # Remove leading whitespace
                stripped_line = line.lstrip()
                # Skip comments and blank lines
                if stripped_line.startswith('#') or not stripped_line:
                    continue
                # Increment the line of code counter
                loc += 1
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return loc


if __name__ == "__main__":
    # Entry point of the script
    main()
