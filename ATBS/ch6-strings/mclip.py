#!/usr/bin/env python3

import sys, pyperclip

TEXT = {
    "agree": """Yes, I agree. That's fine with me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would you consdier making this a monthly donation?""",
}

def main():
    
    if len(sys.argv) != 2 or "--help" in sys.argv:
        print("Usage: python mclip.py [keyphrase]")
        print("Description: Copies the phrase text to the Clipboard.")
        sys.exit()

    key = sys.argv[1]

    if key in TEXT:
        pyperclip.copy(TEXT[key])
        print(f"Text for <<{key}>> has been copied to the clipboard")
    else:
        print(f"There is no text for {key}")

if __name__ == "__main__":
    main()