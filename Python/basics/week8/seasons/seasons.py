# 23/07/2026
# Implement a program that calculates a person's age in minutes.
# Prompt the user for their date of birth in YYYY-MM-DD format.
# Calculate the number of minutes between the birth date and today,
# assuming both dates are at midnight.
# Output the result in English words (not numerals), without using
# the word "and".
# Exit with an error message if the input is not a valid date in the
# required format.
# Also create a separate test file using pytest to thoroughly test
# the helper functions (excluding main()).

# Requirements:
# - Prompt the user for a birth date in YYYY-MM-DD format.
# - Use datetime.date.today() to obtain today's date.
# - Assume both the birth date and today's date are at 00:00:00.
# - Calculate the total number of minutes elapsed.
# - Convert the number into English words.
# - Do not include "and" in the English representation.
# - Exit via sys.exit if the input format is invalid.
# - Ensure the program does not raise uncaught exceptions.

# Steps:
# 1. Import:
#       - date from datetime
#       - sys
#       - inflect (for converting numbers to words)
#
# 2. Create one or more helper functions:
#    - Parse and validate the birth date.
#    - Calculate the elapsed number of days.
#    - Convert days into minutes.
#    - Convert the minute count into English words.
#
# 3. Create main():
#    - Prompt the user for a birth date.
#    - Validate the input.
#    - Calculate the total minutes since birth.
#    - Convert the number to English words.
#    - Print the result followed by "minutes".
#
# 4. In test_seasons.py:
#    - Import the helper function(s) from seasons.py.
#    - Write one or more test functions whose names begin with test_.
#    - Test:
#         * Valid dates.
#         * Leap-year dates.
#         * Invalid date formats.
#         * Correct minute calculations.
#         * Correct English word conversion.
#
# 5. Run the tests using:
#       pytest test_seasons.py

from datetime import date
import sys
import inflect
import re

p = inflect.engine()

def verify_date():
    dob = input("Date of Birth: ")
    
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", dob):
            sys.exit("Invalid date!")

    year, month, day = map(int, dob.split("-"))
    if year < 0 and not 1 <= month <= 12 and not 1 <= day <= 31: 
        sys.exit("Invalid date!")

    return year, month, day

def convert(year, month, day):
    
    birthday = date(year, month, day)
     
    today = date.today()
         
    difference = today - birthday  
    minutes = difference.days * 24 * 60
     
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"

def main():

    y, m, d = verify_date()

    print(convert(y, m, d))

if __name__ == "__main__":
    main()