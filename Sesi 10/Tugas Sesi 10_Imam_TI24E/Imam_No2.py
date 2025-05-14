data_mahasiswa = {}

def tambah_mahasiswa(nim, nama, jurusan, ipk):
    data_mahasiswa[nim] = {
        "Nama": nama,
        "Jurusan": jurusan,
        "IPK": ipk
    }

def tampilkan_semua_data():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.")
    else:
        for nim, info in data_mahasiswa.items():
            print(f"NIM: {nim}, Nama: {info['Nama']}, Jurusan: {info['Jurusan']}, IPK: {info['IPK']}")

def cari_data_mahasiswa(nim):
    if nim in data_mahasiswa:
        info = data_mahasiswa[nim]
        print(f"NIM: {nim}, Nama: {info['Nama']}, Jurusan: {info['Jurusan']}, IPK: {info['IPK']}")
    else:
        print("Data mahasiswa tidak ditemukan.")

def hapus_data_mahasiswa(nim):
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print(f"Data mahasiswa dengan NIM {nim} telah dihapus.")
    else:
        print("Data mahasiswa tidak ditemukan.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah data mahasiswa baru")
        print("2. Tampilkan semua data mahsiswa baru")
        print("3. Cari data mahasiswa berdasarkan NIM")
        print("4. Hapus data mahasiswa berdasarkan NIM")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            nim = input("Masukan NIM: ")
            nama = input("Masukan Nama: ")
            jurusan = input("Masukan Jurusan: ")
            ipk = input("Masukan IPK: ")
            tambah_mahasiswa(nim, nama, jurusan, ipk)
            print("Data mahasiswa berhasil ditambahkan.")
            
        elif pilihan == '2':
            tampilkan_semua_data()
            
        elif pilihan == '3':
            nim = input("Masukan NIM yang dicari: ")
            
            cari_data_mahasiswa(nim)
        elif pilihan == '4':
            nim = input("Masukan NIM ayng ingin dihapus: ")
            
            hapus_data_mahasiswa(nim)
        elif pilihan == '5':
            print("Program Selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silahkan pilih lagi.")
menu()