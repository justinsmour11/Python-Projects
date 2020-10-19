from tkinter import *
from tkinter import filedialog
import shutil
import os
import time



win = Tk()
win.title("Check files")

b1 = Button(win, text="Browse", command=lambda: browseFiles1())
b1.grid(row=0,column=0,padx=10,pady=(30,5))

b2 = Button(win, text="Browse", command=lambda: browseFiles2())
b2.grid(row=1,column=0,padx=10)

b3 = Button(win, text="Copy files", command=lambda: fileCheck())
b3.grid(row=2, column=3,pady=(5,15))

e1 = Entry(win, width=50)
e1.grid(row=0, column=1, columnspan=3, padx=10, pady=(30,5))

e2 = Entry(win, width=50)
e2.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

def fileCheck():

    source = e1.get()
    destination = e2.get()
    files = os.listdir(source)
    currentTime = time.time()
    currentTimeInHours = currentTime / 3600
    
    for i in files:
        fullPath = source + "/" + i
        modTime = os.path.getmtime(fullPath)
        modTimeInHours = modTime / 3600
        if modTimeInHours + 24 >= currentTimeInHours:
            shutil.copy(fullPath, destination)

def browseFiles1():
    win.directory = filedialog.askdirectory()
    e1.insert(END, win.directory)

def browseFiles2():
    win.directory = filedialog.askdirectory()
    e2.insert(END, win.directory)

win.mainloop()
    




