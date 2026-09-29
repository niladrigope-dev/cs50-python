def main():
    name = input ("Enter your name: ")
    x=float(input("what is x? "))
    square("squared value of x: ", x)
    hello(name)


def hello(to="world"):
        print("hello, ", to)

def square(description, n):
    result = pow(n, 2)
    print(description, result)

main()
