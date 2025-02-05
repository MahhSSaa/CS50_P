from datetime import date
import inflect
import sys
import operator

p = inflect.engine()


def main():
    try:
        date_of_birth = input("Date of Birth: ")
        # date.fromisoformat(dob) will check whether dob is a valid date or not
        differences = operator.sub(date.today(), date.fromisoformat(date_of_birth))
        print(convert(differences.days))
    except ValueError:
        sys.exit("Invalid date")


def convert(time):
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
