# 22/07/2026
# Implement a program that overlays a CS50 shirt image onto a user image.
#
# The program expects exactly two command-line arguments:
#   1. The input image file (JPEG or PNG).
#   2. The output image file (JPEG or PNG).
#
# The program should:
#   - Open the input image.
#   - Resize and crop it to match the size of shirt.png.
#   - Overlay shirt.png on top of the image.
#   - Save the final image as the output file.
#
# Exit with an error message if:
#   - The user does not provide exactly two command-line arguments.
#   - The input or output file does not have a valid image extension
#     (.jpg, .jpeg, or .png).
#   - The input and output files have different extensions.
#   - The input file does not exist.

# Steps:
# 1. Import:
#       - sys
#       - PIL.Image
#       - PIL.ImageOps
#
# 2. Verify that exactly two command-line arguments are provided.
#
# 3. Validate file extensions:
#       - Convert extensions to lowercase.
#       - Ensure both files end with:
#           .jpg, .jpeg, or .png
#       - Ensure input and output extensions match.
#
# 4. Open the input image using:
#       Image.open()
#
# 5. Open shirt.png using:
#       Image.open()
#
# 6. Resize and crop the input image to match shirt.png dimensions:
#       ImageOps.fit()
#
# 7. Overlay shirt.png on top of the resized image:
#       Image.paste()
#       Use shirt.png as the mask so transparency is preserved.
#
# 8. Save the final image:
#       Image.save()

import sys
from PIL import Image
from PIL import ImageOps

def cml_verify():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments!")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments!")
        
        if not sys.argv[1].lower().endswith((".png", ".jpg", ".jpeg")):
            sys.exit("Not a valid Image file!")
        
        if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
            sys.exit("The output Image must have the same extension as the input Image!")
    
    except IndexError:
        sys.exit("Can't save image to that file!")

def shirt():
    shirt = Image.open("shirt.png")
    input = Image.open(sys.argv[1])

    resized = ImageOps.fit(input, shirt.size)

    resized.paste(shirt,shirt)
    
    return resized.save(sys.argv[2])

def main():
    try: 
        cml_verify()

        shirt()

    except (FileNotFoundError):
        sys.exit("File does not exist!")

if __name__ == "__main__":
    main()