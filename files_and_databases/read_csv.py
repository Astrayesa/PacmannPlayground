import csv

file = open("data/file.csv", "w")
csv_obj = csv.writer(file)

csv_obj.writerow(["No", "Nama", "Umur"])
csv_obj.writerow(["1", "Budi", "16"])
csv_obj.writerow(["2", "Andi", "18"])
file.close()

file_open = open("data/file.csv", "r")
csv_read_obj = csv.reader(file_open)
for row in csv_read_obj:
    print(row)