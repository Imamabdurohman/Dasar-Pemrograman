# Meminta penguna memasukan 5 nama buah
buah1 = input("Masukan nama buah pertama: ")
buah2 = input("Masukan nama buah kedua: ")
buah3 = input("Masukan nama buah ketiga: ")
buah4 = input("Masukan nama buah keempat: ")
buah5 = input("Masukan nama buah kelima: ")

#Menyimpan nama buah dalam sebuah tuple
tuple = (buah1, buah2, buah3, buah4, buah5)

# Menampilkan tuple tersebut
print("Tuple buah: ", tuple)

# Meminta pengguna memasukan nama buah yang ingiin dicari
cari = input("Masukan nama buah yang ingin dicari: ")

# Memeriksa apakah buah ada dalam tuple
if cari in tuple:
    print(f"{cari} ada dalam tuple.")
else:
    print(f"{cari} tidak ada dalam tuple.")

# Menghitung dan menampilkan jumlah kemunculan setiap buah dalam tuple
for buah in tuple:
    jumlah = tuple.count(buah)
    print(f"Jumlah kemunculan '{buah}': {jumlah}")