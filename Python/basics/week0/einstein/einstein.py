#15/07/2026
#Einstein famous equation "E=mc^2" to calculate Energy. Replicate it to do calculation using Python.
#1. Prompts the user for "mass" (m) which is measured using kg. c: speed of light, 3*(10^8) by default
#2. Returns the final result in format "E: ..."

def equation(mass):
    speed_of_light = 3 * (10 ** 8)
    E = mass * (speed_of_light ** 2)
    return E

def main():
    mass = int(input("m: "))
    print(f"E: {equation(mass)}")

if __name__ == "__main__":
    main()