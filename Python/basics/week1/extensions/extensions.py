#15/07/2026
#Files on computer has their own extensions
#Determine its media type based on its extension
#1. Prompts for a file
#2. Returns the corresponding media type based on extensions

def extension(ext):
    if ext.endswith(".gif"):
        return "image/gif"
    elif ext.endswith(".jpg") | ext.endswith(".jpeg"):
        return "image/jpeg"
    elif ext.endswith(".png"):
        return "image/png"
    elif ext.endswith(".pdf"):
        return "application/pdf"
    elif ext.endswith(".txt"):
        return "text/plain"
    elif ext.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

def main():
    ext = input("File name: ").strip().lower()
    print(extension(ext))

if __name__ == "__main__":
    main()
