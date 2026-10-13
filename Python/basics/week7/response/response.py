# 23/07/2026
# Implement an email validation program.
# Prompt the user for an email address and determine whether it is
# syntactically valid using a third-party validation library.
# Do not use regular expressions (re).
# Print "Valid" or "Invalid" accordingly.

# Requirements:
# - Prompt the user for an email address.
# - Use either:
#     * validator-collection
#       or
#     * validators
#   from PyPI to validate the email address.
# - Do not use the re module.
# - Only validate the email's syntax.
# - Do not check whether the email's domain actually exists.

# Steps:
# 1. Install one of the required libraries:
#       pip install validators
#       or
#       pip install validator-collection
#
# 2. Import the chosen library.
#
# 3. Prompt the user for an email address.
#
# 4. Pass the email address to the library's validation function.
#
# 5. If the email is syntactically valid:
#       - Print "Valid"
#    Otherwise:
#       - Print "Invalid"
#
# 6. Run the program and verify it correctly identifies:
#       - Valid email addresses.
#       - Invalid email addresses.
#       - Missing username/domain.
#       - Invalid characters or formatting.

import validators

def main():
    print(validation(input("What's your email address? ").strip()))

def validation(s):
    if validators.email(s):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()

