def main():
    text = input("Enter text: ")

    print("Words:", count_words(text))
    print("Characters:", count_characters(text))
    print("Most common word:", most_common_word(text))


def count_words(text):
    text1 = text.split()
    return len(text1)


def count_characters(text):
    return len(text)


def most_common_word(text):
    text1 = text.split()
    counts = {}

    for word in text1:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return max(counts, key=counts.get)

if __name__ == "__main__":
    main()
