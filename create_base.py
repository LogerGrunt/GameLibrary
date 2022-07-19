import sqlite3 as sql3

# Now this will be just a python file that we will run to create a new db

# Connedcting to the database that we have

conn = sql3.connect("games.db")

c = conn.cursor()

# Now, we are going to create our table

c.execute("""CREATE TABLE if NOT EXISTS games (
    game_img text
    )""")






# Trying to insert a filepath into the db. Just a quick test.
# c.execute("INSERT INTO games (game_img) VALUES (:filepath)",
#     {
#         "filepath": 'images/Delphian.ico'
#     })


# Time to commit changes to the database
conn.commit()

# And also we need to close the connection
conn.close()