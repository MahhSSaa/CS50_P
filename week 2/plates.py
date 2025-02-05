def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not all(ch.isalnum() for ch in s):
        return False

    flag = False
    for character in s:
        if character.isdigit():
            flag = True
        if character.isalpha() and flag:
            return False

    for character in s:
        if character.isdigit():
            return character != "0"

    return True


if __name__ == "__main__":
    main()
