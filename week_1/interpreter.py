calculator = input("Expression: ")
x, y, z = calculator.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(f"{x + z:.1f}")   
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")   
else:
    print(f"{x / z:.1f}")