# 1. Buatlah aplikasi untuk menentuka tahun kabisat atau bukan
# 2. Buatlah aplikasi untuk menentukan output: negatif, positif, atau nol
# 3. buatlah aplikasi untuk menghitung total yang harus dibayar berdasarkan diskon akhir tahun :
# - Jika total belanjaan lebih dari 100 ribu, maka mendapat diskon 10% 
# - Jika total belanjaan lebih dari 50 ribu, maka mendapat diskon 5% 
# - Jika total belanjaan kurang dari 50 ribu, maka tidak mendapatkan diskon



belanja = float(input("masukan total belanja: "))
if belanja >= 100000 : 
    print (f"anda mendapat diskon 10%, anda membayar: {belanja * (90/100)}")
elif belanja >=50000:
    print (f"anda mendapat diskon 5%, anda membayar: {belanja * (95/100)}")
elif belanja <= 50000:
    print (f"anda tidak mendapatkan diskon anda membayar: {belanja}")