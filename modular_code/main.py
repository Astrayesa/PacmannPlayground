import kelas

def main():
    kelas.load_data()
    while(True):
        menu()
        menu_inp = int( input("Masukan pilihan anda: ") )
        
        if(menu_inp == 1):
            # add data siswa
            nama_siswa = input("Masukan nama siswa: ")
            nilai_tugas = float(input("Masukan nilai tugas siswa: "))
            nilai_ujian = float(input("Masukan nilai ujian siswa: "))
            kelas.add_siswa(nama_siswa, nilai_tugas, nilai_ujian)
            print("Data siswa berhasil diinputkan")

        elif menu_inp == 2:
            # edit nilai siswa
            print("Pilihan edit: ")
            print("1. Nilai tugas")
            print("2. Nilai ujian")
            edit_inp = int(input("Masukan jenis nilai yang ingin diedit: "))
            if edit_inp == 1:
                # edit nilai tugas
                nama_siswa = input("Masukan nama siswa: ")
                nilai_tugas = float(input("Masukan nilai tugas baru siswa: "))
                # buat fungsi edit nilai tugas
                print("Nilai tugas siswa berhasil diupdate")
                pass
            elif edit_inp == 2:
                # edit nilai ujian 
                nama_siswa = input("Masukan nama siswa: ")
                nilai_ujian = float(input("Masukan nilai ujian baru siswa: "))
                kelas.edit_nilai_ujian(nama_siswa, nilai_ujian)
                print("Nilai ujian siswa berhasil diupdate")
            else: 
                print("Pilihan salah")

        elif menu_inp == 3:
            # hapus data siswa
            nama_siswa = input("Masukan nama siswa: ")
            kelas.delete_siswa(nama_siswa)
            print("Berhasil menghapus data siswa")

        elif menu_inp == 4:
            kelas.print_list_siswa()

        elif menu_inp == 5:
            kelas.save_data()
            print("Terimakasih sudah menggunakan program. Bye!")
            break

        else:
            print("Pilihan salah")


def menu():
    print("Menu: ")
    print("1. Menambah data siswa baru")
    print("2. Edit nilai siswa")
    print("3. Hapus data siswa")
    print("4. Tampilkan data siswa")
    print("5. Keluar Program")


if __name__ == "__main__":
    main()