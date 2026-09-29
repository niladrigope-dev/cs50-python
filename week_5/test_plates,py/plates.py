def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not (2 <= len(s) <= 6):
        return False

    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    number_started = False

    for c in s:
        if c.isdigit():
            if not number_started:
                if c == "0":
                    return False
                number_started = True
        elif number_started:
            return False

    return True


if __name__ == "__main__":
    main()