# list_siswa yang menyimpan nama_siswa, nilai_tugas, nilai_ujian.
list_siswa = []

def add_siswa(nama_siswa, nilai_tugas, nilai_ujian):
  if type(nama_siswa) != str:
    return False
  if type(nilai_tugas) != float and type(nilai_tugas) != int:
    return False
  if type(nilai_ujian) != float and type(nilai_ujian) != int:
    return False
  list_siswa.append([nama_siswa, nilai_tugas, nilai_ujian])
  return True

def edit_nilai_ujian(nama_siswa, nilai_ujian_baru):
  # cek apakah nama ditemuakn
  # ....

  for siswa in list_siswa:
    if siswa[0] == nama_siswa:
      siswa[2] = nilai_ujian_baru
  return True

def delete_siswa(nama_siswa):
  for index, siswa in enumerate(list_siswa):
    if siswa[0] == nama_siswa:
      break
  
  list_siswa.pop(index)
  return True

def print_list_siswa():
  print("==================================")
  print("Nama Tugas Ujian")
  for i in list_siswa:
    print(*i)

  print("==================================")