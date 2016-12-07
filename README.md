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
    
And here is the GUI version I added later on - Written in Tkinter, and i used my Tkinter GUI - Application Class Template. It is form another one of my repositories - I have done a few little Tk GUI apps and eventually came up with a template to save time when starting a project - over time I learnt about using classes in an object oriented style of programming and from then on wrote my Tk apps into a class. So the template is a basic GUI setup that creates a  window, with a Container Frame inside. Then I put all of the child widgets within this frame. So all I did was use my class template, and then edit the plain Python versions function to work with SringVar() mand an entry box rather than the input() or raw_input()...here it is:

    #!usr/bin/env python
    import Tkinter
    from Tkinter import *
    import webbrowser
    import time

    # I put everything into this class
    class App():
        def __init__(self, master):
            # Function to handle string concatenation and search
            def doTheSearch():
                address = 'http://www.google.com/#q='
                word = cvt_from.get()
                newWord = address + word
                cvt_to.set(newWord)
                time.sleep(1.5)
                webbrowser.open(newWord)

            # Used to take text from entrybox 
            cvt_to = StringVar()
            # And display the new string to the label
            cvt_from = StringVar()

            # Container Frame / Parent Widget
            frame = Frame(master)
            # Child Widgets
            frame.pack()
            lbl_one = Label(master, bg='Grey', fg='Blue', font='freesansbold, 11', text='\nEnter your Search below \n\nNOTE: If you have multiple words \nuse the (+) symbol to join them. \neg: Words+Like+This\n\n')
            lbl_one.pack()
            ent_one = Entry(master, width=30, textvariable=cvt_from, justify='center', font='freesansbold, 14')
            ent_one.pack()
            btn_two = Button(master, bg='DarkGray', fg='Blue', font='freesansbold,14', text='Go to search results', command=doTheSearch )
            btn_two.pack()
            lbl_two = Label(master, textvariable=cvt_to, bg='DarkGray', relief='ridge')
            lbl_two.pack(fill=BOTH, expand=True)

    # Main config settings for GUI
    root = Tk()
    app = App(root)
    root.title('Python Google Search')
    root.minsize(350,350)
    root.configure(bg='Gray')
    # Magical mainloop
    root.mainloop()


This is the first rough draft at this, and it seems to work well - at least it does what I wanted it to do. I had imagined this being a handy tool to be able to import from any python session and use to search something quickly with 2 lines...an import(which runs the program)...then a search word. I liked that no additional modules are needed, it sums up the power of Python - being able to do a lot with a little.

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

You see how they did their query section of the address a little different to mine, perhaps this is a more reliable way to do it, I don't know. The way I found my method was by opening a google.com search page, entering a search query (the word Python for example), and making a note of how the address in the address bar changed as I clicked search. I found it adds the usual forward slash to an address extension (/) then #q=Python.

So mine uses: 

    http://google.com/#q=Python

The Python google script uses this method: 

    http://google.com/search?q=Python
    
The python one uses string formatting to combine the search string with the uncompleted address - although my first version didn't use string formatting (it just joins/concatenates the 2 strings together to form one) I was very happy when I saw the Python way used the same idea as I came up with...this is the great feeling of progress when learning!

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


