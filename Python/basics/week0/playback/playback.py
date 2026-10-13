#15/07/2026
#Sometimes people needs to speak slower for others to understand
#1. Replace "space" with "..." 
#2. Print the output

def main():
    str_value = input("Enter your prompt: ").strip().replace(" ","..." )
    print(f"{str_value}")

if __name__ == "__main__":
    main()