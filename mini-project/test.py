import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute('DELETE FROM movie WHERE title="Annabele"')
con.commit()

cur.execute("SELECT * FROM movie")
for row in cur.fetchall():
    print(row)