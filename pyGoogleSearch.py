# This asks user for a word to search in Google
# Then concatenates their search request string with the address string
# the address has to be like this to allow it to read as a google search:
# http://www.google.com/#q=   ### With (/#q=) after the (.com)
# The user can enter a group of words as long as they have (+) symbols joining them
# Written and tested with Python 3

import webbrowser

def pyGoogleSearch():
    address = 'http://www.google.com/#q='
    word = raw_input('Enter a word: \n>>> ')
    newWord = address + word
    print'Opening: ', newWord
    webbrowser.open(newWord)

pyGoogleSearch()
