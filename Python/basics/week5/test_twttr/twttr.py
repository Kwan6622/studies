# 22/07/2026
# Reimplement the twttr program using functions.
# Create a shorten() function that removes all vowels
# (A, E, I, O, U) from a string, regardless of case.
# The function should return the modified string.
# Also create a separate test file using pytest to
# thoroughly test the shorten() function.

# Steps:
# 1. Create shorten(word):
#    - Accept a string as input.
#    - Remove all uppercase and lowercase vowels.
#    - Return the resulting string.
#
# 2. Create main():
#    - Prompt the user for a string.
#    - Call shorten().
#    - Print the returned string.
#
# 3. In test_twttr.py:
#    - Import shorten from twttr.py.
#    - Write one or more test functions whose names begin with test_.
#    - Test different scenarios, including:
#      - Strings containing only vowels.
#      - Strings containing no vowels.
#      - Mixed uppercase and lowercase vowels.
#      - Numbers and punctuation (should remain unchanged).
#      - Empty string.
# 4. Run the tests using:
#       pytest test_twttr.py

def main():
    print(shorten(input("Input: ")))


def shorten(word):
    return "".join(letter for letter in word if letter.lower() not in "aioeu")

if __name__ == "__main__":
    main()