# 19/07/2026
# Implement a program that converts dates to ISO 8601 format (YYYY-MM-DD).
# Prompt the user for a date until a valid one is entered.
# Accept either:
#   - MM/DD/YYYY (e.g., 9/8/1636)
#   - Month DD, YYYY (e.g., September 8, 1636)
# Ignore invalid dates and keep prompting.
# Output the date in YYYY-MM-DD format, padding the month and day
# with leading zeroes when necessary.

# Steps:
# 1. Create a list of month names in order.
# 2. Continuously prompt the user for a date.
# 3. Determine which input format was used ('/' or month name).
# 4. Parse the month, day, and year.
# 5. Validate the month and day values.
# 6. Print the date in YYYY-MM-DD format.

import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def verify(date):
    if re.match(r"^\d{1,2}/\d{1,2}/\d{4}$", date):
        print("Format 1")

    elif re.match(r"^[A-Za-z]+ \d{1,2}, \d{4}$", date):
        print("Format 2")

    else:
        print("Invalid") 

def main():
    verify(input("Date: "))

if __name__ == "__main__":
    main()
