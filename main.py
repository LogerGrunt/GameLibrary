from msilib.schema import ComboBox
from textwrap import fill
from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
import tkinter
import sqlite3
import os
from click import edit
import create_base


# Starter code to run the app
root = Tk()
root.title("Epic Delphi Game Lib")
root.iconbitmap = ("images/Delphian.ico")


# Recising the app to be zoomed from the begginning
root.state("zoomed")

# Setting the genres list
genres = [
    "ALL GAMES",
    "ACTION GAMES",
    "MOBA GAMES"
]
# Creating the variable to store the chosen genre
chosen_genre = StringVar()
chosen_genre.set(genres[0])












# Creating the top menu frame
top_frame = LabelFrame(root,height=200,width=200)

# Making the home function for the button
def home():
    # Creating the top panel with buttons:

    # Creating a home button in the top menu of the screen
    home_btn = Button(top_frame,text="HOME",command=home)

    # Creating a drop-down menu for the genres of the games
    genres_list = OptionMenu(top_frame,chosen_genre,*genres)
    # genres_list.config(height=2)
    

    
    # Putting the top panel things on the screen:

    # Putting the home button on the screen
    home_btn.grid(row=0,column=0,ipady=1)

    # If you try to just set a button and an optionmenu sitting together,
    # the optionmenu will become 1 pixel bigger in height than the button
    # In order to resolve that I gave the home button an extra ipad of 1 pixel.
    # Don't like having to put it there, but it works!

    # Putting the dropdown genre menu on the screen
    chosen_genre.set(genres[0])
    genres_list.grid(row=0,column=1)








# Putting the top menu frame on the screen
top_frame.grid(row=0,column=0,columnspan=8,sticky=NS)



home()

root.mainloop()