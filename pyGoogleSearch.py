# This asks user for a word to search in Google
# Then concatenates their search request string with the address string
# the address has to be like this to allow it to read as a google search:
# http://www.google.com/#q=   ### With (/#q=) after the (.com)
# The user can enter a group of words as long as they have (+) symbols joining them
# Written and tested with Python 3

# I tend to avoid raw_input() normally, favouring input() with a type
# but for use on Python 3 it would only accept raw_input

import webbrowser

def pyGoogleSearch():
    address = 'http://www.google.com/#q='
    word = raw_input('Enter a word to search using Google: \n>>> ')
    newWord = address + word
    print'Opening: ', newWord
    webbrowser.open(newWord)

pyGoogleSearch()
