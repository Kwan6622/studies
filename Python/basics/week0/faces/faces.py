#15/07/2026
#Emoticons were the predecessor of emoji, like :) and :(. Nowadays, it's automatically converted to emojis thanks to technology.
#1. Prompts user for a string
#2. Convert the ":)" to "🙂" and ":(" to "🙁"
#3. Returns the output

def convert(user_string):
    user_string = user_string.replace(":)","🙂").replace(":(","🙁")
    return user_string

def main():
    user_string = input("Prompt: ")
    converted = convert(user_string)
    print(converted)

if __name__ == "__main__":
    main()