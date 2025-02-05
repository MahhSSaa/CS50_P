import random

def main():
    # Prompt the user for the level
    level = get_positive_integer("Level: ")

    # Randomly generate an integer between 1 and the specified level
    target_number = random.randint(1, level)

    while True:
        # Prompt the user to guess the integer
        guess = get_positive_integer("Guess: ")

        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break
        
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    main()
