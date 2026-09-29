import random

while True:
    try:
        game = int(input("Level: "))

        if game <= 0:
            continue
        else:
            break

    except ValueError:
        continue

secret = random.randint(1, game)

while True:
    try:
        guess = int(input("Guess: "))

        if guess <= 0:
            continue

        if guess < secret:
            print("Too small!")

        elif guess > secret:
            print("Too large!")

        else:
            print("Just right!")
            break

    except ValueError:
        continue