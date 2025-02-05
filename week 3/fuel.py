def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = get_fuel_percentage(fraction)

            # Output based on the calculated percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            # If there's an error, prompt the user to enter the fraction again
            continue


def get_fuel_percentage(fraction):
    try:
        # Split the input into two parts: X and Y
        x, y = fraction.split("/")
        # Convert both parts to integers
        x = int(x)
        y = int(y)

        # Validate the inputs
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        # Calculate the percentage
        percentage = (x / y) * 100

        # Round the percentage to the nearest integer
        percentage = round(percentage)

        return percentage
    except (ValueError, ZeroDivisionError):
        # Raise the exception to be handled by the calling function
        raise


if __name__ == "__main__":
    main()
