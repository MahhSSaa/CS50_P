import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # Check for command-line arguments
    if len(sys.argv) == 1:
        # No arguments, use a random font
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)

    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # Two arguments, check if font is valid
        font = sys.argv[2]
        if font in figlet.getFonts():
            figlet.setFont(font=font)
        else:
            print(f"Error: '{font}' is not a valid font.")
            sys.exit(1)
    else:
        # Invalid number of arguments or incorrect format
        print("Usage: figlet.py [-f | --font] [font_name]")
        sys.exit(1)

    # Prompt the user for input text
    user_input = input("Input: ")

    # Output the text in the desired font
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
