# 23/07/2026
# Implement a program that counts occurrences of the word "um".
# Create a count() function that returns the number of times "um"
# appears as a standalone word in a string, ignoring case.
# Do not count "um" when it appears as part of another word
# (e.g., "yummy", "album", "umbrella").
# Also create a separate test file using pytest to thoroughly
# test the count() function.

# Requirements:
# - count(text):
#     * Accept a string as input.
#     * Count occurrences of "um" as a whole word only.
#     * Treat uppercase and lowercase equally.
#     * Return the total count as an integer.
#
# Steps:
# 1. Import re (optional) and sys (optional).
# 2. Create count(text):
#    - Search the string for standalone occurrences of "um".
#    - Ignore case.
#    - Do not count "um" inside other words.
#    - Return the total count.
#
# 3. Create main():
#    - Prompt the user for a line of text.
#    - Pass the text to count().
#    - Print the returned count.
#
# 4. In test_um.py:
#    - Import count from um.py.
#    - Write three or more test functions whose names begin with test_.
#    - Test:
#        * A single "um".
#        * Multiple occurrences.
#        * Mixed capitalization ("UM", "Um", "uM").
#        * "um" adjacent to punctuation.
#        * Words containing "um" (e.g., "yummy", "album", "umbrella")
#          should not be counted.
#
# 5. Run the tests using:
#       pytest test_um.py

import re

def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
