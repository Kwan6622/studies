#16/07/2026
#There are rules for custom vehicle plate in Massachusetts
#1. Prompts for a plate
#2. Verify all the requirements in the is_valid function
"""Requirements: 
| STARTS WITH 2 LETTERS 
| MAXIMUM 6 CHARACTERS - MINIMUM OF 2 
| NUMBERS MUST BE AT THE END OF THE PLATE _ STARTING NUBMER CANT BE 0 
| NO PUNCTUATIONS OR SPACES
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False 
    
    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False
    
    numb_reg = False
    for char in s:
        if char.isalpha() and numb_reg == True:
            return False

        if char.isdigit() and numb_reg == False:
            if char == "0":
                return False
            
            numb_reg = True

    return True

if __name__ == "__main__":
    main()