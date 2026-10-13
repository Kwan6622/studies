#19/7/2026
#A Fuel gauge is often comes with fractions to show how much fuel left in the tank.
#Implement a program that prompts a fraction as X/Y, where X is non-negative and Y is positive 
#If 1% or less remain output E instead of the percent, if 99% or more output F
#1. Prompts for a fraction format X/Y 
#2. Catch any errors in a loop and require user to reprompt till correct
#3. Convert into percentage
#4. Output the percentage or E or F corresponding

def convert(fraction):
    x, y = map(int, fraction.strip().split("/"))
            
    if not (0 <= x <= y):
        raise ValueError

    percentage = round((x/y)*100) 

    return "F" if percentage >= 99 else "E" if percentage <= 1 else f"{percentage}%"

def main():
    while True:
        try:
            print(f"{convert(input("Fraction: "))}")
            break

        except (ValueError, ZeroDivisionError):
            pass 

if __name__ == "__main__":
    main()
