text = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
output = print("Output: ", end="")

for character in text:
    if character.casefold() not in vowels:
        print(character, end="")

print()

