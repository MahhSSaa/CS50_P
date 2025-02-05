exception = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

in_put = input("File name: ").lower().strip()

# Check if the input contains a period
if "." in in_put:
    # Find the index of the last period in the input
    index = int(in_put.rindex(".")) + 1
    # Extract the file extension
    result = in_put[index:]
    # Check if the extracted extension is in the dictionary
    if result in exception:
        print(exception[result])
    else:
        print("application/octet-stream")
else:
    # If there is no period in the input, print the default MIME type
    print("application/octet-stream")
