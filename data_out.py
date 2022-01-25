# this is the vault for the answers given by student imput and should be saved - written to a file whan the program quits
import sqlite3
from datetime import datetime


save = sqlite3.connect("random_data.sqlite")
s = save.cursor()
s.execute('DROP TABLE IF EXISTS save_random')
s.execute("""CREATE TABLE save_random (
            rnumber INTEGER,
            rmusic TEXT,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
save.commit()
save.close()

# save the progress of students everytime they succesfully finish a question.
def save_random(number, artist):
    sdata = sqlite3.connect("random_data.sqlite")
    print("trying to write to a database: ")
    s = sdata.cursor()
    s.execute(
        "INSERT INTO save_random VALUES (:number, :artist, :time)",
        {
            'number': number,
            'artist': artist,
            'time': datetime.now()})
    sdata.commit()
    sdata.close()