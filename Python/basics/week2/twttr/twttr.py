#16/07/2026
#During texting, people usually remove vowels to save some time. Ex: Twitter -> Twttr
#Prompts user for a string then return without vowels
#Vowels are ["a", "o", "i", "u", "e"]
#1. Prompts user for a string
#2. Loop through each elements to remove vowels
#3. Returns the result

def convert(prompt):
    return "".join(
        "" if letter.lower() in ["a", "o", "i", "u", "e"] else letter
        for letter in prompt
    )

def main():
    prompt = input("Input: ")
    print("Output:",convert(prompt))

if __name__ == "__main__":
    main()