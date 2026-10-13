# 19/07/2026
# Implement a taqueria ordering system.
# Prompt the user for menu items, one per line, until EOF (Ctrl+D).
# Treat input case-insensitively and ignore items not on the menu.
# After each valid item, display the running total prefixed with '$'
# and formatted to two decimal places.

# Steps:
# 1. Store the menu and prices in a dictionary.
# 2. Continuously prompt the user for an item until EOF.
# 3. Normalize the input (e.g., title case) and verify it exists in the menu.
# 4. If valid, add its price to the running total.
# 5. Print the updated total after each valid item.

def main():
    items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0 

    while True: 
        try:
            item = input("Item: ").strip().title()
            if item in items:
                total += items[item]
                print(f"Total: ${total:.2f}")

        except KeyError:
            pass
        
        except EOFError:
            break

if __name__ == "__main__":
    main()