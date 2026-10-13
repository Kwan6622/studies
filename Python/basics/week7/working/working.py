# 23/07/2026
# Implement a working hours converter.
# Prompt the user for a time range in 12-hour format and convert it
# to the equivalent 24-hour format.
# Accept times with or without minutes.
# Raise a ValueError for invalid formats or invalid times.
# Also create a separate test file using pytest to thoroughly test convert().

# Requirements:
# - convert(s):
#     * Accept a string representing a time range in one of these formats:
#         - 9:00 AM to 5:00 PM
#         - 9 AM to 5 PM
#         - 9:00 AM to 5 PM
#         - 9 AM to 5:00 PM
#     * Convert both times to 24-hour format.
#     * Return the converted string in the format:
#         HH:MM to HH:MM
#     * Raise ValueError if:
#         - The input format is invalid.
#         - Either hour is invalid (not between 1 and 12).
#         - Either minute is invalid (not between 00 and 59).
#         - AM/PM is missing or malformed.
#
# - main():
#     * Prompt the user for working hours.
#     * Print the converted result.

# Steps:
# 1. Create convert(s):
#    - Parse the start and end times.
#    - Verify that the input matches one of the accepted formats.
#    - Extract:
#         * Hour
#         * Optional minutes
#         * AM/PM
#    - Validate the hour and minute values.
#    - Convert each time to 24-hour format:
#         * 12 AM -> 00:MM
#         * 12 PM -> 12:MM
#         * AM (1–11) -> unchanged
#         * PM (1–11) -> hour + 12
#    - Return the formatted string:
#         HH:MM to HH:MM
#
# 2. Create main():
#    - Prompt the user for working hours.
#    - Print the result returned by convert().
#
# 3. In test_working.py:
#    - Import convert() from working.py.
#    - Write three or more test functions whose names begin with test_.
#    - Test:
#         * Valid inputs with minutes.
#         * Valid inputs without minutes.
#         * Mixed formats (one time with minutes, one without).
#         * Midnight (12 AM).
#         * Noon (12 PM).
#         * Invalid hours (0, 13, etc.).
#         * Invalid minutes (60 or greater).
#         * Invalid input formats.
#
# 4. Run the tests using:
#       pytest test_working.py

import re

def main():
        print(convert(input("Hours: ").strip()))

def convert(s):
    if not (match := re.match(r"^0?([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to 0?([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$",s , re.IGNORECASE)):
        raise ValueError("Value Error")

    hour_1, minute_1, time_1, hour_2, minute_2, time_2 = match.groups()

    if time_1 == "PM":
        if 1 <= int(hour_1) <= 11:
            hour_1 = str(int(hour_1) + 12)
        elif hour_2 == "12":
            hour_2 = "00"

        if 1 <= int(hour_2) <= 9:
            hour_2 = f"0{hour_2}"


    elif time_2 == "PM":
        if 1 <= int(hour_2) <= 11:
            hour_2 = str(int(hour_2) + 12)
        elif hour_1 == "12":
            hour_1 = "00"

        if 1 <= int(hour_1) <= 9:
            hour_1 = f"0{hour_1}"


    minute_1 = minute_1 if minute_1 else ":00"
    minute_2 = minute_2 if minute_2 else ":00"

    return f"{hour_1}{minute_1} to {hour_2}{minute_2}"

if __name__ == "__main__":
    main()
