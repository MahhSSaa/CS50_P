import sys
import csv


def main():
    """Main function to handle command-line arguments and process the CSV files."""
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv"):
        sys.exit("Not a CSV file")

    data = read_csv(input_file)
    processed_data = process_data(data)
    write_csv(output_file, processed_data)


def read_csv(file_path):
    """Read the CSV file and return its data."""
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        sys.exit(f"Could not read {file_path}")


def write_csv(file_path, data):
    """Write the processed data to a new CSV file."""
    fieldnames = ["first", "last", "house"]
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        sys.exit(f"Error: Could not write to file '{file_path}'. {e}")


def process_data(data):
    """Process the input data by splitting names into first and last names."""
    processed_data = []
    for row in data:
        try:
            last, first = row["name"].split(", ")
            processed_row = {"first": first, "last": last, "house": row["house"]}
            processed_data.append(processed_row)
        except ValueError:
            sys.exit(f"Error: Name format incorrect in row: {row}")
    return processed_data


if __name__ == "__main__":
    main()
