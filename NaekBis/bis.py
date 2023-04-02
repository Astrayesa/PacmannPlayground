class Bis:
  def __init__(self, kapasitas_penumpang, km_perjalanan, biaya_per_km):
    self.kapasitas_penumpang = kapasitas_penumpang
    self.km_perjalanan = km_perjalanan
    self.biaya_per_km = biaya_per_km
    self.penumpang = {}
    self.total_pendapatan = 0

  def scan_in(self, id, nama):
    if self.kapasitas_penumpang > len(self.penumpang):
      # data penumpang berupa [nama, kilomter_penumpang_naik]
      self.penumpang[id] = [nama, self.km_perjalanan]
      return f"Scan-in berhasil, selamat datang {nama}"
    return "Bis penuh, scan-in gagal"

  def scan_out(self, id):
    km_penumpang = self.km_perjalanan - self.penumpang[id][1]
    biaya_penumpang = km_penumpang * self.biaya_per_km
    self.total_pendapatan += biaya_penumpang
    self.penumpang.pop(id)
    return f"Perjalan = {km_penumpang} KM\nTotal = {biaya_penumpang}"

  def update_nama_penumpang(self, id, nama_baru):
    self.penumpang[id][0] = nama_baru
    return f"Nama penumpang berhasil diubah menjadi {nama_baru}"

  def pendapatan(self):
    return self.total_pendapatan

  def perjalanan(self, km):
    self.km_perjalanan += km
  