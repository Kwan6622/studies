# 20/07/2026
# Implement an "Adieu" farewell program.
# Prompt the user for names, one per line, until EOF (Ctrl+D).
# Assume at least one name will be entered.
# After EOF, output a farewell message listing the names using
# proper English grammar with commas and "and" (Oxford comma).

# Steps:
# 1. Create a list to store the names.
# 2. Continuously prompt the user for names until EOF.
# 3. Append each name to the list.
# 4. After EOF:
#    - If there is one name, print it directly.
#    - If there are two names, join them with " and ".
#    - If there are three or more names, separate them with commas,
#      using ", and" before the final name (Oxford comma).
# 5. Print the final farewell message:
#    "Adieu, adieu, to ..."

import inflect

p = inflect.engine()

names = []

def main():
    while True:
        try:
            names.append(input("Name: "))

        except EOFError:
            print("\n")
            print(f"Adieu, adieu, to {p.join(names)}")
            break


if __name__ == "__main__":
    main()
