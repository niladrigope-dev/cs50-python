import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.match(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)
    if not matches:
        raise ValueError
    hour1 = matches.group(1)
    minute1 = matches.group(2)
    ampm1 = matches.group(3)
    hour2 = matches.group(4)
    minute2 = matches.group(5)
    ampm2 = matches.group(6)

    if minute1 is None:
        minute1 = "00"
    if minute2 is None:
        minute2 = "00"

    hour1 = int(hour1)
    minute1 = int(minute1)

    hour2 = int(hour2)
    minute2 = int(minute2)

    if not 1 <= hour1 <= 12 or not 1 <= hour2 <= 12:
        raise ValueError

    if not 0 <= minute1 <= 59 or not 0 <= minute2 <= 59:
        raise ValueError

    if hour1 == 12 and ampm1 == "AM":
        hour1 = 0
    if hour1 == 12 and ampm1 == "PM":
        hour1 = 12
    if 1<=hour1<=11 and ampm1 == "AM":
        pass
    if 1<=hour1<=11  and ampm1 == "PM":
        hour1 += 12

    if hour2 == 12 and ampm2 == "AM":
        hour2 = 0
    if hour2 == 12 and ampm2 == "PM":
        hour2 = 12
    if 1<=hour2<=11 and ampm2 == "AM":
        pass
    if 1<=hour2<=11  and ampm2 == "PM":
        hour2 += 12
    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


if __name__ == "__main__":
    main()
