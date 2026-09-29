def convert(text):
    print(text.replace(":)", "🙂").replace(":(", "🙁"))

def main():
    text = input ("What message would you like to convert? ")
    convert(text)

main()        