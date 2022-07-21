from tkinter import *
from PIL import *
import os


# I will use this file in order to make a little window that pops up when a user wants to add a game to the library.

def create_game():
    cr_sc = Toplevel()
    cr_sc.title("Add a new game to the library")

    app_width = 200
    app_height = 200

    screen_width = cr_sc.winfo_screenwidth()
    screen_height = cr_sc.winfo_screenheight()

    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_width/2)

    cr_sc.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    cr_sc.attributes('-topmost', 'true')

    # Creating the functions for the user to enter the game's data
    pls_name = Label(cr_sc,text="ENTER GAME NAME:")
    pls_name.grid(row=0,column=0)

    enter_name = Entry(cr_sc,width=30)
    enter_name.grid(row=1,column=0)

    pls_des = Label(cr_sc,text="ENTER GAME DESCRIPTION:")
    pls_des.grid(row=3,column=0)
    
    enter_des = Entry(cr_sc,width=30)
    enter_des.grid(row=4,column=0)

