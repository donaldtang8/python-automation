# will google map search address passed in as arguments or clipboard content
import webbrowser, sys, pyperclip

sys.argv

# Check if command arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]);
else:
    address = pyperclip.paste();

webbrowser.open('https://www.google.com/maps/place/' + address);