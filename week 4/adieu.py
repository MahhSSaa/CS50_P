import inflect
import sys

def main():
    p = inflect.engine()
    names = []

    print("Enter names one per line. Press Ctrl-D (or Ctrl-Z on Windows) to finish.")

    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    # Generate the formatted string
    if names:
        farewell = f"Adieu, adieu, to {p.join(names)}"
        print(farewell)

if __name__ == "__main__":
    main()
