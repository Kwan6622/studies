# 22/07/2026
# Reimplement the Home Federal Savings Bank program using functions.
# Create a value() function that determines the monetary value of a greeting.
# The function should return:
#   - 0 if the greeting starts with "hello"
#   - 20 if the greeting starts with "h" (but not "hello")
#   - 100 otherwise
# Treat greetings case-insensitively.
# Assume the input string has no leading spaces.
# Only main() should call print().
# Also create a separate test file using pytest to thoroughly
# test the value() function.

# Steps:
# 1. Create value(greeting):
#    - Accept a string as input.
#    - Convert the string to lowercase.
#    - Return:
#        * 0 if it starts with "hello".
#        * 20 if it starts with "h" but not "hello".
#        * 100 otherwise.
#
# 2. Create main():
#    - Prompt the user for a greeting.
#    - Call value().
#    - Print the returned value.
#
# 3. In test_bank.py:
#    - Import value from bank.py.
#    - Write three or more test functions whose names begin with test_.
#    - Test different scenarios, including:
#      - Greetings starting with "hello".
#      - Greetings starting with "h" but not "hello".
#      - Greetings not starting with "h".
#      - Mixed uppercase and lowercase input.
#      - Single-letter greetings such as "H".
#
# 4. Run the tests using:
#       pytest test_bank.py

def main():
    print(f"${value(input("Greeting: "))}")

def value(greeting):
    return 0 if greeting.lower().startswith("hello") else 20 if greeting.lower().startswith("h") else 100 

if __name__ == "__main__":
    main()
