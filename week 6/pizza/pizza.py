import sys
import os
import csv
from tabulate import tabulate

def main():
    # Check if the user provided exactly one command-line argument
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    # Check if the file has a .csv extension
    if not file_path.endswith('.csv'):
        print("Not a CSV file")
        sys.exit(1)

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File does not exist")
        sys.exit(1)

    # Read the CSV file
    headers, rows = read_csv(file_path)

    # Print the table formatted as ASCII art using tabulate
    print(tabulate(rows, headers=headers, tablefmt='grid'))

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Get the headers
            rows = [row for row in reader]  # Get the rows
            return headers, rows
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point of the script
    main()
