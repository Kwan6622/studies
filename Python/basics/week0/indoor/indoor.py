#15/07/2026
#Prompt user for a string then returns it in all lowercase
#1. takes an input from user
#2. returns the output in lowercase (keep punctuation and whitespace the same as input)

def main():
    prompt = input("Prompt: ").lower()
    print(f"{prompt}")

if __name__ == "__main__":
    main()