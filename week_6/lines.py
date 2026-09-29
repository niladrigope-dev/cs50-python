import sys
import os

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


if not (sys.argv[1]).endswith(".py"):
    sys.exit("Not a Python file")

if not os.path.exists(sys.argv[1]):
    sys.exit("File does not exist")

file = open(sys.argv[1])

count = 0

for line in file:
    if line.strip() == "":
        continue
    elif line.strip().startswith("#"):
        continue
    else:
        count += 1

print (count)
