from tkinter import *
import webbrowser

#Create parent window and assign to win
win = Tk()
win.title("Create your own content!")
#Submit button contain createPage function
b1 = Button(win, text="SUBMIT", command=lambda: createPage())
b1.pack()

#Text box content to add to web page
t1 = Text(win)
t1.pack()

    
def createPage():
    #open web page and append
    h = open("createpage.html", "w")
    #get contents from text box and write into html doc
    h.write("<html><body><h1>{}</h1></body></html>".format(t1.get("1.0",END)))
    h.close()

    #open page in new window
    webbrowser.open("createpage.html", new=1)
    
    


