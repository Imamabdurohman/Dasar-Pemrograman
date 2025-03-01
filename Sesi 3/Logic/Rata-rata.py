# 1. Menghitung nilai rata-rata matematika untuk kelas 10C yang berjumlah 5 orang
s_1 = float(input("masukan nilai ahmad: "))
s_2 = float(input("masukan nilai jarkom: "))
s_3 = float(input("masukan nilai bayu: "))
s_4 = float(input("masukan nilai anton: "))
s_5 = float(input("masukan nilai lery: "))

Rata_Rata = (s_1 + s_2 + s_3 + s_4 + s_5)/5
print (f"Rata_Rata: {Rata_Rata}" )

# 2. Menghitung nilai rata-rata seorang siswa dari 5 mata pelajaran (IPA, IPS, MTK, ENGLISH, INDONESIA)
a = float(input("masukan nilai IPA: "))
b = float(input("masukan nilai IPS: "))
c = float(input("masukan nilai MTK: "))
d = float(input("masukan nilai B. Indonesia: "))
e = float(input("masukan nilai B. Inggris: "))

rata_rata = (a + b + c + d + e) / 5
print(f"rata-rata: {rata_rata}")

nilai = [s_1, s_2, s_3, s_4, s_5]

# 3. Mengecek nilai llulus atau tidak lulus dengan kireteria
# - Dinyatakan lulus, jika nilai rata-rata dari semuanya lebih dari 75
# - Dinyatakan lulus, jika hanya 2 mata pelajaran yang nilainay dibawah 50
# - Mendapatkan nilai sempurna (100) dari salah satu mata pelajaran
nilai_50 = 2
if (s_1 < 50):
    nilai_50 += 1
if (s_2 < 50):
    nilai_50 += 1
if (s_3 < 50):
    nilai_50 += 1
if (s_4 < 50):
    nilai_50 += 1
if (s_5 < 50):
    nilai_50 += 1

if Rata_Rata >= 75:
    print("lulus")
elif (nilai.count(100) >=1):
    print("Lulus, sempurna karna mendapat nilai 100 dari salah satu mata pelajaran")
elif(nilai == 2):
    print("Lulus, karena hanya 2 mata pelajaran yang nilainya dibawah 50")
else:
    print("Tidak lulus")