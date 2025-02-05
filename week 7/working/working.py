import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    # Define a regular expression pattern to match the time formats
    pattern = re.compile(r'^(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)$')

    # Match the pattern against the input string
    match = pattern.match(s)
    if not match:
        raise ValueError("Invalid time format")

    # Extract the components of the time range
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Convert hours and minutes to integers, defaulting minutes to 00 if not provided
    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute else 0

    # Validate minutes
    if start_minute >= 60 or end_minute >= 60:
        raise ValueError("Invalid minutes")

    # Convert start time to 24-hour format
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    # Convert end time to 24-hour format
    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    # Format the times as HH:MM
    start_time_24 = f"{start_hour:02}:{start_minute:02}"
    end_time_24 = f"{end_hour:02}:{end_minute:02}"

    return f"{start_time_24} to {end_time_24}"

if __name__ == "__main__":
    main()
