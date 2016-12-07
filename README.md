# pyGoogleSearch
Asks the user what they want to search
Then opens a Google results page for their word/s in their browser

* Can be run as a standalone program
* Can be called in as a module
* Can be run in either a Shell or Terminal (interactive session)
* Needs no extra modules (webbrowser comes with Python as a default module)
* Written and tested in Python 3
* TO SEARCH MULTIPLE WORDS add the (+) symbol to join them (multiple+words+like+this)

This was just me playing around

I stumbled upon the module webbrowser and loved the fact you can open a web browser at any url with literally 2 lines of code:
    
    import webbrowser
    webbrowser.open('http://google.com')
    
And wondered if you could actually get Python to do a Google search, and display the results without adding too much code. Turns out you can - with almost NO extra code

So I looked at a browser address for google.com and noted what happens to the address when you enter a search query. This revealed that it is easy to add a search query into the web address to show the results page instead of a search page

You do it like this...heres a standard google link:

http://google.com

And heres what the address looks like if you search the word "Python" :

http://google.com/#q=Python

So I used this in my code by creating the variable address with this inside:

http://google.com/#q=

Then all I had to do was take input from the user (asking what to search for) then concatenate/join the 2 strings together to create a new variable called newAddress. The newAddress gets given to the webbrowser.open command.

The 2 strings together make the full address for a google search results page, for whatever the user enters. 

Heres my plain version of this - I had to use raw_input() for python 3 and just input():

    import webbrowser

    def pyGoogleSearch():
        address = 'http://www.google.com/#q='
        word = raw_input('Enter a word: \n>>> ')
        newWord = address + word
        print'Opening: ', newWord
        webbrowser.open(newWord)

    pyGoogleSearch()
    

This is the first rough draft at this, I had imagined this being a handy tool to be able to import from any python session and use to search something quickly with 2 lines...an import(which runs the program)...then a search word. I liked that no additional modules are needed, it sums up the power of Python - being able to do a lot with a little.

I put it into a function for convenience, I hope to add the argument ability to it - so you could just go:

    pyGoogleSearch(Anything)

With one line/command to run a search from Python and show a search results page in a web Browser

Things I might do in time:
---------------------------

* Add the browser select feature of webbrowser into it
* Add the new tab or new window choice into it
* Make it functional as an importable module
* 'Maybe' add a Tkinter GUI interface to it over time - seems a bit small for a GUI as it is but I may do it for practice


Update (07/12/2016) Python has something similar:
------------------------------
I was looking through the scripts that come with Python and theres a few handy little tools built in. Python does have a google script as-well, a little bit more complex than mine, If you want to have  a look, I found it in Python 3's files on a Windows System. I haven't looked on Ubuntu or Raspbian so I caouldn't tell you the location of Python's folder without looking it up.

On Windows look in your main C: directory and look for Python34:
C:\Python34\Tools\Scripts\google.py 
and it looks like this:

    #! /usr/bin/env python3
    import sys, webbrowser

    def main():
        args = sys.argv[1:]
        if not args:
            print("Usage: %s querystring" % sys.argv[0])
            return
        list = []
        for arg in args:
            if '+' in arg:
                arg = arg.replace('+', '%2B')
            if ' ' in arg:
                arg = '"%s"' % arg
            arg = arg.replace(' ', '+')
            list.append(arg)
        s = '+'.join(list)
        url = "http://www.google.com/search?q=%s" % s
        webbrowser.open(url)

    if __name__ == '__main__':
        main()

    

NOTE
-----
I did add a GUI version about an hour after creating the original code and repo. I used Tkinter for convenience. The GUI prompts the user to enter a search word (something to search for on google) then it uses the same function from the text version, with adjustments to the input method to perform the task of opening a search results page for the input word. 

I used the entrybox this time and StringVar() to play with the input/strings

The function behaves the same really - it takes a string from from the user, and joins it onto the unfinished Google search query URL, so whatever is entered gets joined to the URL directly.

The function is linked to the Button to get the results...what I did was have the full URL of the page display in the lower section (Label) and have a time delay of about a second before loading the browser. Then the browser opens up with the search results.

I did this quite quickly so it may be rough around the edges.

At the time of writing I plan to put the whole thing into a class, and maybe have a reset or restart function.

It is normally common practice for me to put QUIT buttons into my TKinter apps, but on my Windows system (used to write this) the quit function causes a crash no matter what I use it on...so you will have to use the [X] at the top right of the window.(This isn't a problem on my other systems - Ubuntu and Raspbian)

I want to keep the GUI and text versions completely seperate, because I would love for the text one to end up as a module - even if it's just for my own use!


