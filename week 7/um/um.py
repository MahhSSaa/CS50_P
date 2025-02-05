import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Find all occurrences of "um" as a whole word using regular expression
    matches = re.findall(r'\bum\b', s, flags=re.IGNORECASE)

    return len(matches)


if __name__ == "__main__":
    main()
