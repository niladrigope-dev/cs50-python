from datetime import date

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:

    date_input = input("Date: ")

    try:

        if "/" in date_input:
            x, y, z = date_input.split("/")

            month = int(x)
            day = int(y)
            year = int(z)

        else:
            month, rest = date_input.split(" ", 1)
            day, year = rest.split(",")

            month = months[month]
            day = int(day)
            year = int(year)

        valid_date = date(year, month, day)

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except (KeyError, ValueError):
        pass