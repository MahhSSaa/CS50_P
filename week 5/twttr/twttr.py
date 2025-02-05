def main():
    text = input("Input: ")
    output = shorten(text)
    print("Output:", output)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for character in word:
        if character.casefold() not in vowels:
            result += character
    return result

if __name__ == "__main__":
    main()
