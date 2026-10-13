# 23/07/2026
# Implement an IPv4 address validator.
# Prompt the user for an IPv4 address and determine whether it is valid.
# A valid IPv4 address:
#   - Consists of exactly four numbers separated by periods (.).
#   - Each number must be an integer between 0 and 255 (inclusive).
# Output True if the address is valid, otherwise False.
# Also create a separate test file using pytest to thoroughly test validate().

# Requirements:
# - validate(ip):
#     * Accept a string representing an IPv4 address.
#     * Return True if:
#         - The address contains exactly four octets.
#         - Every octet is numeric.
#         - Every octet is between 0 and 255 (inclusive).
#     * Return False otherwise.
#
# - main():
#     * Prompt the user for an IPv4 address.
#     * Print the result returned by validate().

# Steps:
# 1. Create validate(ip):
#    - Split the input string using ".".
#    - Verify that exactly four parts exist.
#    - For each part:
#        * Check that it contains only digits.
#        * Convert it to an integer.
#        * Verify that it is between 0 and 255.
#    - Return True if all checks pass; otherwise return False.
#
# 2. Create main():
#    - Prompt the user for an IPv4 address.
#    - Print the result of validate().
#
# 3. In test_numb3rs.py:
#    - Import validate() from numb3rs.py.
#    - Write two or more test functions whose names begin with test_.
#    - Test:
#        * Valid IPv4 addresses.
#        * Numbers outside the range (e.g., 256, 275).
#        * Too few or too many octets.
#        * Non-numeric octets.
#        * Empty octets or malformed addresses.
#
# 4. Run the tests using:
#       pytest test_numb3rs.py

import re

def validate(ip):
    pattern = r"^\d+\.\d+\.\d+\.\d+$"

    if not re.match(pattern, ip):
        return False

    parts = ip.split(".")

    for part in parts:
        if int(part) > 255:
            return False

    return True

def main():
    print(validate(input("IPv4 Address: ")))

if __name__ == "__main__":
    main()