import sqlite3

conn = sqlite3.connect("siswa.db")

cursor = conn.cursor()

sql_create_table = """
CREATE TABLE IF NOT EXISTS siswa (
    nama TEXT,
    jenis_kelamin TEXT,
    km_naik INTEGER,
    km_turun INTEGER,
    biaya_per_km INTEGER
);
"""

cursor.execute(sql_create_table)

cursor.execute("SELECT * FROM siswa;")

for row in cursor.fetchall():
    print(row)