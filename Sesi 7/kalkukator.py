def menu():
    print ("menu operator")
    print ("1. tambah")
    print ("2. kurang")
    print ("3. kali")
    print ("4. bagi")
    print ("5. exit")
def tambah (x, y):
    return x + y
def kurang (x, y):
    return x - y
def kali (x, y):
    return x * y
def bagi (x, y):
    if y != 0:
        return x/y
    else :
        return "Tidak bisa membagi dengan nol"
pilihan = input("pilih menu: ")
if pilihan in ['1', '2', '3', '4', '5']:
    angka1 = float(input("Masukan angka pertama: "))
    angka2 = float(input("Masukan angka kedua: "))
    
    if pilihan == '1':
        print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")