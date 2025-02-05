months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date_input = input("Date: ").strip()

    # Try parsing the date in MM/DD/YYYY format
    try:
        month, day, year = date_input.split("/")
        month, day, year = int(month), int(day), int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break
    except ValueError:
        pass

    # Try parsing the date in 'Month Day, Year' format
    try:
        month_day, year = date_input.rsplit(",", 1)
        month_name, day = month_day.split()
        day, year = int(day), int(year)
        month = months.index(month_name) + 1
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break
    except (ValueError, IndexError):
        pass
