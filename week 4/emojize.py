import emoji

def main():
    # Prompt the user for a string in English
    user_input = str(input("Input: ").strip())

    # Convert the input string to its emojized version
    emojized_output = emoji.emojize(user_input, language='alias')

    # Output the emojized version
    print("Output:", emojized_output)

if __name__ == "__main__":
    main()
