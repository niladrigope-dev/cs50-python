import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for _ in range(3):
            try:
                z = int(input(f"{x} + {y} = "))
                if z == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(x+y)
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1:
                return 1
            elif level == 2:
                return 2
            elif level == 3:
                return 3
            elif level < 1 or level > 3:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()