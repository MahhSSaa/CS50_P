import random

def main():
    level = get_level()  # Prompt the user for the level
    score = 0  # Initialize the score

    # Generate and present 10 math problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y  # Calculate the correct answer
        tries = 0  # Initialize the number of attempts

        # Allow up to 3 tries for each problem
        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))  # Prompt the user for an answer
                if answer == correct_answer:
                    score += 1  # Increment the score if the answer is correct
                    break
                else:
                    print("EEE")  # Indicate incorrect answer
                    tries += 1  # Increment the number of attempts
            except (ValueError, EOFError):
                print("EEE")  # Indicate incorrect answer if input is invalid
                tries += 1  # Increment the number of attempts

        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")  # Show the correct answer after 3 incorrect attempts

    print(f"Score: {score}")  # Display the final score

def get_level():
    while True:
        try:
            level = int(input("Level: "))  # Prompt the user for the level
            if level in [1, 2, 3]:
                return level  # Return the valid level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except (ValueError, EOFError):
            print("Invalid input. Please enter a number.")  # Handle invalid input

def generate_integer(level):
    # Generate a random integer based on the level
    if level == 1:
        return random.randint(0, 9)  # Single digit for level 1
    elif level == 2:
        return random.randint(10, 99)  # Two digits for level 2
    elif level == 3:
        return random.randint(100, 999)  # Three digits for level 3
    else:
        raise ValueError("Invalid level")  # Raise an error if the level is not valid

if __name__ == "__main__":
    main()
