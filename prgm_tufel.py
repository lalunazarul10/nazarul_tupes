
karyawan = []

def tambah_karyawan(nama, umur, jabatan):
    data = (nama, umur, jabatan)
    karyawan.append(data)
    print(f"Karyawan {nama} berhasil ditambahkan.")

def tampilkan_karyawan():
    if not karyawan:
        print("Belum ada data karyawan.")
    else:
        print("\nData Karyawan:")
        for i, data in enumerate(karyawan, start=1):
            print(f"{i}. Nama: {data[0]}, Umur: {data[1]}, Jabatan: {data[2]}")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Karyawan")
        print("2. Tampilkan Karyawan")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            nama = input("Masukkan nama karyawan: ")
            umur = input("Masukkan umur karyawan: ")
            jabatan = input("Masukkan jabatan karyawan: ")
            tambah_karyawan(nama, umur, jabatan)
        elif pilihan == "2":
            tampilkan_karyawan()
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()