# 22/07/2026
# Implement a program that displays a CSV file as a formatted ASCII table.
# The program expects exactly one command-line argument: the name or
# path of a CSV file containing pizza menu data.
# Read the CSV file and display its contents as a table using the
# 'tabulate' library with the "grid" table format.
# Exit with an error message if:
#   - The user does not provide exactly one command-line argument.
#   - The file does not have a .csv extension.
#   - The file does not exist.

# Steps:
# 1. Import sys, csv, and tabulate.
# 2. Verify that exactly one command-line argument is provided.
# 3. Verify that the filename ends with ".csv".
# 4. Attempt to open the CSV file.
#    - If the file cannot be opened, exit with an error message.
# 5. Read the CSV file using csv.reader().
# 6. Store:
#    - The first row as the table headers.
#    - The remaining rows as the table data.
# 7. Use tabulate() with:
#    - headers=<headers>
#    - tablefmt="grid"
# 8. Print the formatted table.

import sys
from tabulate import tabulate
import csv

def cml_verify():
    try: 
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments!")
    
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments!")
        
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file!")
    
    except FileNotFoundError:
        sys.exit("File does not exist!")

def main():
    cml_verify()
    
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)

        print(tabulate(reader, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
