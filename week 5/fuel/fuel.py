def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)

            # Output based on the calculated percentage
            gauge(percentage)
            break
        except (ValueError, ZeroDivisionError, UnboundLocalError):
            # If there's an error, prompt the user to enter the fraction again
            continue


def convert(fraction):
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




def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
