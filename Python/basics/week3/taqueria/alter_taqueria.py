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

    order = {}

    total = 0 

    try:
        while True:   
            item = input("Item: ").strip().title()
            if item in items.keys():
                if item in order:
                    order[item] += 1
                else:
                    order[item] = 1

            for food in order:
                total += order[food] * items[food] 

    except KeyError:
        pass
    
    except EOFError:
        print("Total: {total}$")
        

if __name__ == "__main__":
    main()