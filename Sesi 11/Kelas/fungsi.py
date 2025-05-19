from datetime import datetime

def hitungUmur(tahunLahir):
    tahunIni = datetime.now().year
    umur = tahunIni - tahunLahir
    return umur

tahunLahir = int(input ("Masukan Tahun lahir: "))
umur = hitungUmur(tahunLahir)
print("Umur", umur, "Tahun")

# date time = untuk memanggil tahun sekarang
