# 20/07/2026
# Implement an emoji conversion program.
# Prompt the user for a string containing emoji codes or aliases.
# Convert any valid emoji codes (e.g., :thumbs_up:) and aliases
# into their corresponding emoji characters.
# Output the converted string.

# Steps:
# 1. Prompt the user for an input string.
# 2. Use an emoji conversion method/library to replace codes and aliases.
# 3. Convert all valid emoji codes into their corresponding emojis.
# 4. Print the final emojized string.

import emoji

def main():
    try:
        print(f"Output: {emoji.emojize(input("Input: ").strip(), language='alias')}")
    except (KeyError, ValueError):
        pass

if __name__ == "__main__":
    main()