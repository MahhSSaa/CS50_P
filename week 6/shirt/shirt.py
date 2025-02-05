import sys
import os
from PIL import Image, ImageOps


def main():
    input_file, output_file = validate_args(sys.argv)
    overlay_shirt(input_file, output_file)


def validate_args(args):
    if len(args) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(args) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    input_file = args[1]
    output_file = args[2]

    valid_extensions = (".jpg", ".jpeg", ".png")

    if not (
        input_file.lower().endswith(valid_extensions)
        and output_file.lower().endswith(valid_extensions)
    ):
        print("Invalid output")
        sys.exit(1)

    if (
        os.path.splitext(input_file)[1].lower()
        != os.path.splitext(output_file)[1].lower()
    ):
        print("Input and output have different extensions")
        sys.exit(1)

    if not os.path.isfile(input_file):
        print("Input does not exist")
        sys.exit(1)

    return input_file, output_file


def overlay_shirt(input_file, output_file):
    # Open the input image and the shirt image
    shirt = Image.open("shirt.png")
    user_image = Image.open(input_file)
    w, h = shirt.size
    # Resize and crop the input image to match the shirt image size
    user_image = ImageOps.fit(user_image, (w, h))
    # Overlay the shirt image onto the input image
    user_image.paste(shirt, (0, 0), shirt)
    # Save the result
    user_image.save(output_file)
    print(f"Output saved as '{output_file}'")


if __name__ == "__main__":
    main()
