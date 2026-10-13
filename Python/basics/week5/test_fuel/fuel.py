# 21/07/2026
# Reimplement the Fuel Gauge program using functions.
# Create a convert() function that converts a fraction (X/Y)
# into a percentage, and a gauge() function that returns the
# appropriate fuel gauge display.
# Only main() should handle user input and output.
# Also create a separate test file using pytest to thoroughly
# test both convert() and gauge().

# Requirements:
# - convert(fraction):
#     * Accept a string in the format "X/Y".
#     * X must be a non-negative integer.
#     * Y must be a positive integer.
#     * Return the percentage rounded to the nearest integer (0–100).
#     * Raise ValueError if:
#         - X or Y is not an integer.
#         - X is greater than Y.
#     * Raise ZeroDivisionError if Y is 0.
#
# - gauge(percentage):
#     * Return "E" if percentage <= 1.
#     * Return "F" if percentage >= 99.
#     * Otherwise return "<percentage>%".

# Steps:
# 1. Create convert(fraction):
#    - Split the input into X and Y.
#    - Convert both values to integers.
#    - Validate the input.
#    - Calculate and round the percentage.
#    - Return the percentage as an integer.
#
# 2. Create gauge(percentage):
#    - Return "E" if the percentage is <= 1.
#    - Return "F" if the percentage is >= 99.
#    - Otherwise return the formatted percentage string.
#
# 3. Create main():
#    - Prompt the user for a fraction.
#    - Call convert().
#    - Pass the result to gauge().
#    - Print the returned gauge string.
#
# 4. In test_fuel.py:
#    - Import convert and gauge from fuel.py.
#    - Write two or more test functions whose names begin with test_.
#    - Test convert() with:
#        * Valid fractions.
#        * X greater than Y.
#        * Y equal to 0.
#        * Non-integer input.
#        * Boundary values (0/1, 1/1, etc.).
#    - Test gauge() with:
#        * Empty ("E") cases.
#        * Full ("F") cases.
#        * Normal percentage values.
#
# 5. Run the tests using:
#       pytest test_fuel.py


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break

        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = map(int, fraction.strip().split("/"))

    if y == 0:
        raise ZeroDivisionError

    if not (0 <= x <= y):
        raise ValueError

    return round((x / y) * 100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
