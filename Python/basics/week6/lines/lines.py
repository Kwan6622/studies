# 22/07/2026
# Implement a program that counts the number of lines of code (LOC)
# in a Python source file.
# The program expects exactly one command-line argument: the name or
# path of a Python (.py) file.
# Count only lines containing actual code, excluding blank lines and
# comment lines. A comment line is any line whose first non-whitespace
# character is '#'. Docstrings are NOT considered comments.
# Exit with an error message if:
#   - The user does not provide exactly one command-line argument.
#   - The file does not have a .py extension.
#   - The file does not exist.

# Steps:
# 1. Import sys.
# 2. Verify that exactly one command-line argument is provided.
# 3. Verify that the filename ends with ".py".
# 4. Attempt to open the file.
#    - If the file cannot be opened, exit with an error message.
# 5. Initialize a counter for lines of code.
# 6. Read the file line by line.
# 7. For each line:
#    - Remove leading/trailing whitespace.
#    - Skip the line if it is empty.
#    - Skip the line if it starts with '#'.
#    - Otherwise, increment the line counter.
# 8. Print the total number of lines of code.

import sys

def cml_verify():
    try: 
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments!")
    
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments!")
        
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file!")
    
    except FileNotFoundError:
        sys.exit("File does not exist!")
    
def count():
    lines = 0

    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip().startswith("#"):
                continue
            
            elif line.strip() == "":
                continue

            else:
                lines += 1

    return lines

def main():

    cml_verify()

    print(count())
    
if __name__ == "__main__":
    main()
