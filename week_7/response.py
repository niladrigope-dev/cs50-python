import validators

email = input("What's your email adress? ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
