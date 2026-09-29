import sys
import csv
import os
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not (sys.argv[1]).endswith(".csv"):
    sys.exit("Not a CSV file")

if not os.path.exists(sys.argv[1]):
    sys.exit("File does not exist")

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)

    print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
