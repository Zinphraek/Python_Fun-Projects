#! python3
# mapIt.py - Launches a map in the browser using an address
# from the command line or clipboard.

import webbrowser, sys, pyperclip

# Checking whetehr arguments were provided in the command line
if len(sys.argv) > 1:
    # Getting the address from the command line
    address = ' '.join(sys.argv[1:])
else:
    # Getting the address from the clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
