import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments ")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid input")
if not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")
input_p , input_e = sys.argv[1].lower().split(".")
output_p , output_e = sys.argv[2].lower().split(".")
if not input_e == output_e:
    sys.exit("Input and output have different extensions")
if not os.path.exists(sys.argv[1]):
    sys.exit("Input does not exist")
img = Image.open(sys.argv[1])
shirt = Image.open("shirt.png")
img = ImageOps.fit (img, shirt.size)
img.paste(shirt , (0,0) , shirt)
img.save(sys.argv[2])