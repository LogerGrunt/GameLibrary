import sqlite3
from turtle import update
from tkinter import *
from PIL import *
import os
from tkinter import filedialog
import sqlite3
from click import edit


# I will use this file in order to make a little window that pops up when a user wants to add a game to the library.

def create_game():


    cr_sc = Toplevel()
    cr_sc.title("Add a new game to the library")

    app_width = 210
    app_height = 300

    screen_width = cr_sc.winfo_screenwidth()
    screen_height = cr_sc.winfo_screenheight()

    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_width/2)

    cr_sc.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    cr_sc.attributes('-topmost', 'true')

    # Making a submit function
    def submit():
        conn = sqlite3.connect("games.db")
        c = conn.cursor()
        c.execute("SELECT * FROM games")
        aid = len(c.fetchall())
        c.execute("INSERT INTO games (game_name, game_des, game_filepath, game_genre, game_id) VALUES (:game_name, :game_des, :game_filepath, :game_genre, :game_id)",
        {
            "game_name": enter_name.get(),
            "game_des": enter_des.get(),
            "game_filepath": enter_filepath.get(),
            "game_genre": enter_genre.get(),
            "game_id": (str(int(aid) + 1))
        })
        conn.commit()
        conn.close()
        cr_sc.destroy()


    def add_data():
        cr_sc.filename = filedialog.askopenfilename(initialdir="",title="Select A File",filetypes=((".EXE files", "*.exe"),("all", "*.*")))
        enter_filepath.insert(0,str(cr_sc.filename))


    # Creating the functions for the user to enter the game's data
    pls_name = Label(cr_sc,text="ENTER GAME NAME:")
    pls_name.grid(row=0,column=0)

    enter_name = Entry(cr_sc,width=30)
    enter_name.grid(row=1,column=0)

    pls_des = Label(cr_sc,text="ENTER GAME DESCRIPTION:")
    pls_des.grid(row=3,column=0)
    
    enter_des = Entry(cr_sc,width=30)
    enter_des.grid(row=4,column=0)

    pls_genre = Label(cr_sc,text="ENTER GAME GENRE:")
    pls_genre.grid(row=5,column=0)
    
    enter_genre = Entry(cr_sc,width=30)
    enter_genre.grid(row=6,column=0)


    pls_filepath = Label(cr_sc,text="ENTER GAME FILEPATH:")
    pls_filepath.grid(row=7,column=0)
    
    enter_filepath = Entry(cr_sc,width=30)
    enter_filepath.grid(row=8,column=0)





    # Button that wll trigger the add_data() function
    btn_filepath = Button(cr_sc,text="Choose file",command=add_data)
    btn_filepath.grid(row=9,column=0)   

    # Creating a submit button
    submit_btn = Button(cr_sc,text="ADD GAME",command=submit)
    submit_btn.grid(row=10,column=0)

