from sub.module import *

while(True):
    print("\nMenu")
    print("1. scan-in")
    print("2. scan-out")
    print("3. cetak daftar penumpang")
    print("4. update kilometer")
    print("5. keluar")

    menu = int(input("Pilih menu di atas: "))
    if menu == 1:
        nama_penumpang = input("Masukan nama penumpang: ")
        jenis_kelamin = input("Masukan jenis kelamin: ")
        scan_in(data_bis, nama_penumpang, jenis_kelamin)
    elif menu == 2:
        nama_penumpang = input("Masukan nama penumpang: ")
        scan_out(data_bis, nama_penumpang)
    elif menu == 3:
        cetak_daftar_penumpang(data_bis)
    elif menu == 4:
        km_jalan = int(input("Masukan jarak perjalanan bis: "))
        perjalanan(data_bis, km_jalan)
    elif menu == 5:
        exit()
    else:
        print("Pilihan tidak sesuai, silahkan pilih berdasarkan menu")

