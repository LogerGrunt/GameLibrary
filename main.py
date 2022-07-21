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
import add_game


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
top_menu = LabelFrame(root,height=200,width=200)

# Making the home function for the button
def home():
    # Creating the top panel with buttons:

    # Creating a home button in the top menu of the screen
    home_btn = Button(top_menu,text="HOME",command=home)

    # Creating a drop-down menu for the genres of the games
    genres_list = OptionMenu(top_menu,chosen_genre,*genres)
    
    # Since I'm not going to be adding each game manualy into the code, I will try to make a function that will collect the user's input and will turn it into the game for the library.
    # I'm going to create a separate window for the user's input.
    # This will be the button that will redirect the user to the window to add a game to their library.
    add_game_btn = Button(top_menu,text="ADD GAME",command=add_game.create_game)

    
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

    # Putting the "ADD GAME" button on the screen
    add_game_btn.grid(row=0,column=2,ipady=1)








# Putting the top menu frame on the screen
top_menu.grid(row=0,column=0,columnspan=8,sticky=NS)


create_base
home()

root.mainloop()