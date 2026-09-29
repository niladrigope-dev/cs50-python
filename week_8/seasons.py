from datetime import date
import sys
import inflect


def main():
    birth_date = input("Date of Birth: ")
    try:
        birth = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")
    x = minutes(birth)
    p = inflect.engine()
    kk = p.number_to_words(x, andword = "")
    kk = kk.capitalize()
    print(f"{kk} minutes")

def minutes(birth):
    time = date.today() - birth
    minutes = time.days * 24 * 60
    return minutes


if __name__ == "__main__":
    main()
