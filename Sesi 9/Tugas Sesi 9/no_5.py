daftar_belanja=[]
for i in range(5):
    item = input(f"Masukan item belanja {i+1}: ")
    daftar_belanja.append(item)
print("List daftar belanja: ", daftar_belanja)

hapus = input("Masukan nama item yang sudah dibeli: ")

if hapus in daftar_belanja:
    daftar_belanja.remove(hapus)
    print("daftar belanja setelah di perbarui: ")
else:
    print("item tidal ditemukan dalam daftar")

print("List daftar belanja: ", daftar_belanja)