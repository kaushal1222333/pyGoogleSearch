# Ben Woodfield
# Written in Python 3
# 02/12/2016

# 03/12/2016 - Wrapped everything in a class

'''
    I decided to write up a Tk version for the google search function I wrote
    It asks you what you want to search for, Shows the full URL its displaying
    Then opens a browser and takes you to the search results for what you entered
    eg: it does the search for you

    To Do:
    I want to put the whole thing into a class
    I would like to have a browser selection
    And also choose if the browser opens a Tab or Window
    
'''
__Author__  = 'Ben Woodfield'
__Project__ = 'pyGoogleSearch - GUI version'
__Date__   = '02/12/2016'

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

        # Widgets 
        frame = Frame(master)
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
