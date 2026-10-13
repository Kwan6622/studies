#16/05/2026
#nutrition information for the 20 most frequently consumed raw fruits from the FDA
#1. Prompts for a fruit (case-insensitive) 
#2. Output number of calories in one portion of that fruit based on FDA poster
#Ignore imputs that are incorrect. 

def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    fruit = input("Item: ").lower()
    if fruit in fruits:
        print("Calories:",fruits[fruit])


if __name__ == "__main__":
    main()