def main():
    s = input("Input: ")
    result = shorten(s)
    print(result)

def shorten(word):
    result = ""
    for c in word:
        if c.lower() not in "aeiou":

            result += c
    return result







if __name__ == "__main__":
    main()
