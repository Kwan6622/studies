# 19/07/2026
# Implement a grocery list program.
# Prompt the user for grocery items, one per line, until EOF (Ctrl+D).
# Treat input case-insensitively.
# After EOF, output each unique item in uppercase, sorted alphabetically,
# prefixed with the number of times it was entered.

# Steps:
# 1. Create a dictionary to store each item and its count.
# 2. Continuously prompt the user for an item until EOF.
# 3. Normalize the input (e.g., convert to lowercase).
# 4. Update the item's count in the dictionary.
# 5. Sort the dictionary's keys alphabetically.
# 6. Print each item's count and name in uppercase.

def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().lower()

            grocery_list[item] = grocery_list.get(item,0) + 1     

        except EOFError:
            break
            
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")     

if __name__ == "__main__":
    main()
