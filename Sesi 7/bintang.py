for i in range(5):
    x='*'
    x=x*i
    print(f'{x:<10}')

print("\n=========================================\n")
for i in range(5):
    x='*'
    x=x*i
    print(f'{x:^10}')

print("\n=========================================\n")
def pyramid_terbalik(tinggi):
    for i in range(tinggi, 0, -1):
        print (' ' * (tinggi - i) + '*' * (2 * i - 1))
tinggi_pyramid = int(input("Masukan tinggi pyramid: "))
pyramid_terbalik (tinggi_pyramid)

print("\n=========================================\n")
def pola(tinggii):
    for i in range (1, tinggii + 1):
        print ('*' * i)
tinggi_pola = int(input("Masukan tinggi: "))
pola (tinggi_pola)

print("\n=========================================\n")
def persegi_panjang (panjang, lebar):
    for i in range (lebar):
        print ('*' * panjang)
panjang_pp = int(input("Masukan panjang: "))
lebar_pp = int(input("Masukan lebar"))
persegi_panjang(panjang_pp, lebar_pp)