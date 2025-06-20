import pandas as pd
import os

# Path file input dan output
file_input = r'D:\KULIAH\Semester 2\Dasar Pemrograman\UTS\jadwal_dosen.xlsx'
file_output = r'D:\KULIAH\Semester 2\Dasar Pemrograman\UTS\jadwal_dosen_booked.xlsx'

# Baca file excel
try:
    df = pd.read_excel(file_input)
    print("Data berhasil dibaca.\n")
except FileNotFoundError:
    print("File tidak ditemukan.")
    exit()

# Tampilkan 5 data pertama
print("Contoh data:")
print(df.head())

# Minta input booking dari user
print("\n=== Booking Jadwal Baru ===")
nama_dosen = input("Nama Dosen: ")
mata_kuliah = input("Mata Kuliah: ")
hari = input("Hari (cth: Senin): ")
jam = input("Jam (cth: 08:00 - 10:00): ")
ruang = input("Ruang: ")

# Tambahkan ke DataFrame
booking = {
    'Nama Dosen': nama_dosen,
    'Mata Kuliah': mata_kuliah,
    'Hari': hari,
    'Jam': jam,
    'Ruang': ruang
}

df = pd.concat([df, pd.DataFrame([booking])], ignore_index=True)

# Simpan ke file baru
df.to_excel(file_output, index=False)
print(f"\n✅ Booking berhasil disimpan ke: {file_output}")
