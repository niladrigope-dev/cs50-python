def main():
    s = input("Input: ")
    result(s)

def result(s):
    for c in s:
        if c.lower() not in "aeiou":
            print(c, end=(""))


    


if __name__ == "__main__":
    main()