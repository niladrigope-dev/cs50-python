import pyfiglet
import sys

if len(sys.argv)==3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
    elif sys.argv[2] not in pyfiglet.FigletFont.getFonts():
            sys.exit("invalid usage")
elif len(sys.argv) != 1:
    sys.exit("Invalid usage")
    
text = input ("Input: ")


if len(sys.argv)==1:
    f = pyfiglet.figlet_format(text)

elif len(sys.argv)==3:
    f = pyfiglet.figlet_format(text, font=sys.argv[2])


print (f)