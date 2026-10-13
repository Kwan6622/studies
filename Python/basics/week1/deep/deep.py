#15/07/2026
#From "The Hitchhiker’s Guide to the Galaxy" by Douglas Adams there is a "Great Question of Life, the Universe and Everything…" 
#The answer from the book was forty two
#1. Prompts the user for the answer to "Great Question of Life, the Universe and Everything"
#2. If answer is 42, forty-two or forty two (case insensitive) returns Yes
#3. Else returns No

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    match answer.strip().lower():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

if __name__ == "__main__":
    main()