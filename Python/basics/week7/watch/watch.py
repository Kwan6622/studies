# 23/07/2026
# Implement a YouTube URL parser.
# Prompt the user for a string of HTML and extract the YouTube video URL
# from the src attribute of an iframe element.
# Convert the embedded YouTube URL into its shorter youtu.be format.
# Return None if no valid YouTube embed URL is found.
# Also create a separate test file using pytest to thoroughly test parse().

# Requirements:
# - parse(s):
#     * Accept a string containing HTML.
#     * Locate the src attribute of an iframe element.
#     * Accept embedded YouTube URLs in one of these formats:
#         - http://youtube.com/embed/<id>
#         - https://youtube.com/embed/<id>
#         - https://www.youtube.com/embed/<id>
#     * Return:
#         - "https://youtu.be/<id>" if a valid embedded URL is found.
#         - None otherwise.
#
# - main():
#     * Prompt the user for HTML.
#     * Print the result returned by parse().

# Steps:
# 1. Create parse(s):
#    - Search the HTML for an iframe's src attribute.
#    - Verify that the URL is a valid YouTube embed URL.
#    - Extract the video's ID.
#    - Construct and return the shortened URL:
#          https://youtu.be/<video_id>
#    - Return None if no valid embedded URL exists.
#
# 2. Create main():
#    - Prompt the user for HTML.
#    - Print the value returned by parse().
#
# 3. In test_watch.py:
#    - Import parse() from watch.py.
#    - Write two or more test functions whose names begin with test_.
#    - Test:
#        * http://youtube.com/embed/...
#        * https://youtube.com/embed/...
#        * https://www.youtube.com/embed/...
#        * HTML without an iframe.
#        * HTML with a non-YouTube src.
#        * Invalid or malformed URLs.
#
# 4. Run the tests using:
#       pytest test_watch.py

import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if match := re.search(r'<iframe src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)">', s, re.IGNORECASE):
        return f"https://youtu.be/{match.group(1)}"
    return "None"

if __name__ == "__main__":
    main()
