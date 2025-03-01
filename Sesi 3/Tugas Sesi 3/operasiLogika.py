def uji(a, b, c):
    if isinstance(a, str) and isinstance(b, int) and isinstance(c, float):
        return "Tipe input valid"
    else:
        return "Tipe input tidak valid"

# Kasus uji
print(uji("Halo", 10, 3.14))  # Tipe input valid
print(uji(100, 10, 3.14))  # Tipe input tidak valid
print(uji("Tes", "20", 2.5))  # Tipe input tidak valid
print(uji("Python", 5, 2.0))  # Tipe input valid
