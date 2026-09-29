def main():
    while True:
        try:
            fuel = input("Fraction: ")
            percentage = convert(fuel)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    

if __name__ == "__main__":
    main()
