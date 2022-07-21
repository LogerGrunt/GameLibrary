from tkinter import *
from PIL import *
import os
from tkinter import filedialog

root = Tk()

def create_game():
    # Defining the function for choosing the filepath
    def add_data():
        root.filename = filedialog.askopenfilename() #(initialdir="",title="Select A File",filetypes=((".EXE files", "*.exe"),("all", "*.*")))
        enter_filepath.insert(0,str(root.filename))
    

    enter_filepath = Entry(root,width=30)
    enter_filepath.pack()

    btn_filepath = Button(root,text="Choose file",command=add_data)
    btn_filepath.pack()

create_game()

root.mainloop()