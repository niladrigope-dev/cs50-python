import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    parts = ip.split(".")
    if not len(parts) == 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        number = int(part)
        if not 0 <= number <= 255:
            return False
        if len(part) > 1 and part[0] == "0":
            return False
    return True
...


if __name__ == "__main__":
    main()
