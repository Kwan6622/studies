# 22/07/2026
# Implement a program that cleans and reformats student data in a CSV file.
# The program expects two command-line arguments:
#   1. The name/path of an existing input CSV file.
#   2. The name/path of a new output CSV file.
# The input CSV contains two columns:
#   - name (formatted as "Last, First")
#   - house
# The output CSV should contain three columns:
#   - first
#   - last
#   - house
# Split each student's name into separate first and last names and
# write the reformatted data to the output file.
# Exit with an error message if:
#   - The user does not provide exactly two command-line arguments.
#   - The input file cannot be opened.

# Steps:
# 1. Import sys and csv.
# 2. Verify that exactly two command-line arguments are provided.
# 3. Attempt to open the input CSV file.
#    - If it cannot be opened, exit with an error message.
# 4. Create the output CSV file.
# 5. Read the input file using csv.DictReader().
# 6. Create a csv.DictWriter() with the field names:
#       ["first", "last", "house"]
# 7. Write the header row to the output file.
# 8. For each student:
#    - Split the "name" field into:
#         last, first = name.split(", ")
#    - Write a new row containing:
#         first, last, and house.
# 9. Close both files.

import sys
import csv 

def cml_verify():
    try: 
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        
        if not sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            sys.exit("Not a CSV file!")
    
    except FileNotFoundError:
        sys.exit("File does not exist!")

def main():

    cml_verify()

    with open(sys.argv[1]) as infile, open(sys.argv[2], "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first":first, "last":last, "house":row["house"]})

        sys.exit()
        
if __name__ == "__main__":
    main()
