import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression for validating an IPv4 address
    pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                         r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                         r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                         r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    if pattern.match(ip):
        return True
    return False

if __name__ == "__main__":
    main()
