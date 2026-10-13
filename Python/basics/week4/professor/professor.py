# 20/07/2026
# Implement a math problem generator similar to Little Professor.
# Prompt the user for a difficulty level (1, 2, or 3).
# Generate 10 addition problems using random numbers with the chosen
# number of digits.
# Allow the user up to 3 attempts for each problem.
# Display "EEE" after incorrect answers and reveal the answer after
# 3 failed attempts.
# Track and display the user's final score out of 10.

# Steps:
# 1. Import the random module.
# 2. Create get_level():
#    - Prompt the user for a level.
#    - Validate that the level is 1, 2, or 3.
#    - Reprompt until a valid level is entered.
#
# 3. Create generate_integer(level):
#    - Generate a random non-negative integer with the specified number
#      of digits.
#    - Raise ValueError if level is not 1, 2, or 3.
#
# 4. In main():
#    - Get the user's chosen level.
#    - Generate 10 random X + Y problems.
#    - Prompt the user to solve each problem.
#    - Allow up to 3 attempts for each question.
#    - Print "EEE" for incorrect answers.
#    - Show the correct answer after 3 failed attempts.
#    - Count correct answers and display the final score.

import random

def main():
    score = 0

    level = get_level()
    for _ in range(10):
        try:
            counter = 0
            a, b = generate_integer(level)

            while True:    
                
                if counter == 3:
                    print(f"{a} + {b} = {a+b}")
                    break
                
                answer = int(input(f"{a} + {b} = "))

                if answer == (a+b):
                    score +=1
                    break

                else: 
                    print("EEE")
                    counter += 1
                    continue
        
        except ValueError:
            print("EEE")
            counter += 1
            continue


    print(f"Final Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            
            if level in [1,2,3]:
                return level 
            else:
                raise ValueError
    
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        minimum, maximum = 0, 9

    elif level == 2:
        minimum, maximum = 10, 99

    else:
        minimum, maximum = 100, 999

    return random.randint(minimum, maximum), random.randint(minimum, maximum)

if __name__ == "__main__":
    main()