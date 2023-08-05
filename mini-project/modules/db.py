import sqlite3

con = None
cur = None

def setup():
    global con
    con = sqlite3.connect("tutorial.db")
    global cur
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
    return con, cur

def save_movie(title: str, year: int, score: float):
    # simpan ke database 
    cur.execute(f"""INSERT INTO movie VALUES ("{title}", "{year}", "{score}")""")
    con.commit()

def get_all_movie():
    # tampilkan isi database saat ini
    cur.execute("SELECT * FROM movie")
    for row in cur.fetchall():
        print(row)