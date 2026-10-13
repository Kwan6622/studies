# 20/07/2026
# Implement a FIGlet text generator.
# The program accepts either zero or two command-line arguments.
# If no arguments are provided, render the text using a random font.
# If two arguments are provided, the first must be -f or --font,
# and the second must be a valid FIGlet font name.
# If the arguments are invalid, exit with an error message.
# Prompt the user for a string and output it in the selected font.

# Steps:
# 1. Import sys, random and pyfiglet.
# 2. Check the number of command-line arguments.
# 3. If there are no arguments, randomly choose a font.
# 4. If there are two arguments:
#    - Verify the first argument is -f or --font.
#    - Verify the second argument is a valid font.
#    - Exit with an error message if either check fails.
# 5. Prompt the user for the input text.
# 6. Render the text using the selected FIGlet font.
# 7. Print the rendered ASCII art.

import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

def convert():
    if len(sys.argv) == 1:
       figlet.setFont(font=random.choice(figlet.getFonts()))

    elif len(sys.argv) == 3:
        if not sys.argv[1] == "-f" or sys.argv[1] == "--font":
            sys.exit("Invalid second System Arguement!")
            
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid Font!")
        else:
            figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("Invalid amount of System Argument!")

    return f"Output: \n{figlet.renderText(input("Input: "))}"

def main():
    try:    
        print(convert())

    except SystemError:
        sys.exit("An Error occured! Try again!")

if __name__ == "__main__":
    main()