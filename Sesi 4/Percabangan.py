angka = 4
jenis = "ganjil"
if angka % 2 == 0:
    jenis = "genap"

print("%s adalah bilangan %s"%(angka, jenis))



nilai = int(input("masukan nilai: "))
grade='E'
if nilai >=85:
    grade = 'A'
elif nilai >=75:
    grade = 'B'
elif nilai >=65:
    grade = 'C'
elif nilai >=55:
    grade = 'D'

print ("grade anda adalah %s"%grade)

