#15/07/2026
#In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.”
#Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. 
#The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.
#1. Prompt for a greeting
#2. Check if the greeting is Hello | Starts with H | or None
#3. Returns "$money" based on the greeting $0 | $20 | $100

def money(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    return 100

def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${money(greeting)}")

if __name__ == "__main__":
    main()