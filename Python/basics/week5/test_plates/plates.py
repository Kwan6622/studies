# 22/07/2026
# Reimplement the Vanity Plates program using functions.
# Create an is_valid() function that checks whether a license plate
# satisfies all required rules and returns True or False.
# Only main() should handle user input and output.
# Also create a separate test file using pytest to thoroughly
# test the is_valid() function.

# Requirements for a valid plate:
# - Length must be between 2 and 6 characters.
# - The first two characters must be letters.
# - Plates may contain only letters and digits.
# - Numbers, if present, must come at the end.
# - The first number cannot be 0.

# Steps:
# 1. Create is_valid(s):
#    - Accept a string as input.
#    - Check that the length is between 2 and 6.
#    - Verify the first two characters are letters.
#    - Ensure all characters are alphanumeric.
#    - If numbers appear:
#        * The first number is not 0.
#        * No letters appear after a number.
#    - Return True if all rules are satisfied, otherwise False.
#
# 2. Create main():
#    - Prompt the user for a license plate.
#    - Call is_valid().
#    - Print "Valid" or "Invalid".
#
# 3. In test_plates.py:
#    - Import is_valid from plates.py.
#    - Write four or more test functions whose names begin with test_.
#    - Test different scenarios, including:
#      - Valid license plates.
#      - Invalid lengths (too short or too long).
#      - First two characters not both letters.
#      - Plates containing punctuation or spaces.
#      - Numbers appearing before letters.
#      - First number being 0.
#      - Plates with only letters.
#      - Plates ending with valid numbers.
#
# 4. Run the tests using:
#       pytest test_plates.py


def main():
    print(is_valid(input("Plate: ")))

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return "Invalid" 
    
    if not s[0:2].isalpha():
        return "Invalid" 

    if not s.isalnum():
        return "Invalid" 
    
    numb_reg = False
    for char in s:
        if char.isalpha() and numb_reg == True:
            return "Invalid" 

        if char.isdigit() and numb_reg == False:
            if char == "0":
                return "Invalid" 
            
            numb_reg = True

    return "Valid"


if __name__ == "__main__":
    main()