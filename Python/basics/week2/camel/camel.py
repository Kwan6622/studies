#16/07/2026
#camelCase if widely use in variable naming, in constrast Python recommend using snake_case
#Implement a program that takes a camelCase and output snake_case
#1. Prompts for a camelCase
#2. Loop through the input to tranform it into snake_case
#3. Output the result

def convert(case):
    return "".join(
        "_" + letter.lower() if letter.isupper() else letter
        for letter in case
    )
    
    """
    container = []

    for letter in case:
        if letter.isupper():
            container.append("_")
            letter = letter.lower()

        container.append(letter)

    return "".join(container)
    """

def main():
    case = input("camelCase: ").strip()
    print("snake_case: " + convert(case))

if __name__ == '__main__':
    main()