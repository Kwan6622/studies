#15/07/2026
#Tip is a culture in American. Most people tip around 15% of the meal's worth. Create a calculation to find out how much you want to tip.
#1. Prompts for an amount of money
#2. Prompts for a tip percentage
#3. Convert those to float to do calculations
#4. Returns the amount of money needed for the tip

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = d.replace("$","")
    d = float(d)
    return d


def percent_to_float(p):
    # TODO
    p = p.replace("%","")
    p = float(p) / 100
    return p

if __name__ == "__main__":
    main()