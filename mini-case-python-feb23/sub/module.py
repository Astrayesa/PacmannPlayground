import sqlite3
# modul.py
data_bis = {
    "penumpang": [],
    "kilometer_perjalanan" : 0,
    "kapasitas_penumpang": 10,
    "biaya_per_km" : 10_000,
    "pendapatan": 0
}

def init(data_bis, kapasitas_penumpang_inp, km_jalan, biaya_per_km):
  data_bis["kapasitas_penumpang"] = kapasitas_penumpang_inp
  data_bis["kilometer_perjalanan"] = km_jalan
  data_bis['biaya_per_km'] = biaya_per_km

def cetak_daftar_penumpang(data_bis):
  print("Nama\tJK\tKM Masuk")
  for i in data_bis["penumpang"]:
    print(f"{i[0]}\t{i[1]}\t{i[2]}")

def perjalanan(data_bis, km):
  data_bis["kilometer_perjalanan"] += km

def scan_in(data_bis, nama_penumpang, jenis_kelamin):
  data_bis["penumpang"].append([nama_penumpang, jenis_kelamin, data_bis["kilometer_perjalanan"]])
  print("Data penumpang berhasil dimasukan")

def scan_out(data_bis, nama_penumpang):
  idx_penumpang = -1
  for idx, data in enumerate(data_bis["penumpang"]):
    if data[0] == nama_penumpang:
      idx_penumpang = idx
      break

  if idx_penumpang == -1:
    print(f"Penumpang dengan nama {nama_penumpang} tidak ditemukan")
    return False
  
  # db insert
  conn = sqlite3.connect("siswa.db")
  cursor = conn.cursor()

  sql_insert = f"""
  INSERT INTO siswa (nama, jenis_kelamin, km_naik, km_turun, biaya_per_km) VALUES
  (
    "{data_bis["penumpang"][idx][0]}", 
    "{data_bis["penumpang"][idx][1]}", 
    {data_bis["penumpang"][idx][2]}, 
    {data_bis["kilometer_perjalanan"]},
    {data_bis["biaya_per_km"]}
    )
  """

  cursor.execute(sql_insert)

  conn.commit()

  km_perjalanan_penumpang = data_bis["kilometer_perjalanan"] - data_bis["penumpang"][idx][2] # kilometer sekarang - kilometer saat naik
  biaya_penumpang = data_bis["biaya_per_km"] * km_perjalanan_penumpang
  print(f"Kamu perlu membayar sebesar {biaya_penumpang} setelah menempuh perjalanan sejauh {km_perjalanan_penumpang}")

  data_bis["penumpang"].pop(idx)
  return True