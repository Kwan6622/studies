# 20/07/2026
# Implement a number guessing game.
# Prompt the user for a positive integer level (n).
# Randomly generate a number between 1 and n (inclusive).
# Continuously prompt the user to guess the number until it is guessed correctly.
# Ignore invalid (non-positive) integer inputs and reprompt.
# Output whether each valid guess is too small, too large, or correct.

# Steps:
# 1. Import the random module.
# 2. Prompt the user for a positive integer level until valid.
# 3. Generate a random integer between 1 and the chosen level.
# 4. Continuously prompt the user for a guess.
# 5. Validate that the guess is a positive integer.
# 6. Compare the guess with the random number:
#    - If the guess is smaller, print "Too small!"
#    - If the guess is larger, print "Too large!"
#    - If the guess is equal, print "Just right!" and exit.

import random

def main():
    
    while True:
        try:
            level = int(input("Level: "))
            
            if level > 0:
                break
        except ValueError:
            pass
        
    number = random.randint(1,level)

    while True:
        try:
            guess = int(input("Guess: "))
            
            if guess <= 0:
                continue

        except ValueError:
            continue

        if guess > number:
            print("Too large!")

        elif guess < number:
            print("Too small!")

        else:
            print("Just right!")
            break
        
if __name__ == "__main__":
    main()