from modules.db import setup, save_movie, get_all_movie

con, cur = setup()

# ambil inputan dari user
title = input("Masukan judul film: ")
year = int(input("Masukan tahun film: "))
score = float(input("Masukan nilai film: "))

save_movie(title, year, score)

get_all_movie()