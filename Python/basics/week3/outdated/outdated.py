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

def convert(date):
    if "/" in date:
        month, day, year = map(int, date.split("/"))
        if (1 <= month <= 12) and (1 <= day <= 31) and (year > 0):
            return f"{year:04}-{month:02}-{day:02}" 
        else: 
            raise ValueError
            
    elif ", " in date:
        month_day, year = date.split(", ")
        month, day = month_day.split()
        
        
        if month.title() not in months:
            raise KeyError 
            
        if (1 <= int(day) <= 31) and (int(year) > 0):
            return f"{int(year):04}-{months.index(month) + 1:02}-{int(day):02}" 
        else:
            raise ValueError
            
    else:
        raise ValueError

def main():
    while True:
        try:
            print(convert(input("Date: ")))
            break
        
        except (KeyError, ValueError):
            continue

if __name__ == "__main__":
    main()