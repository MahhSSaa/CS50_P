# Sample plan dictionary for testing purposes
plan = [
    {"start hour": 7, "end hour": 8, "meal": "breakfast time"},
    {"start hour": 12, "end hour": 13, "meal": "lunch time"},
    {"start hour": 18, "end hour": 19, "meal": "dinner time"},
]


def main():
    time = input("What time is it? ").lower().strip()
    time = convert(time)

    for a in plan:
        if time >= float(a["start hour"]) and time <= float(a["end hour"]):
            print(a["meal"])


def convert(time):
    change_value = 0.0
    if "a.m" in time:
        time = time.replace(" a.m", "")
    elif "p.m" in time:
        time = time.replace(" p.m", "")
        change_value = 12.0

    hour, minute = time.strip().split(":")
    resul_time = float(hour) + change_value + (float(minute) / 60)
    return resul_time


if __name__ == "__main__":
    main()
