def main():
    x = input("Masukkan nilai x: ")
    y = input("Masukkan nilai y: ")

    bool_x = bool(int(x) == 1) if x else False
    bool_y = bool(int(y) == 1) if y else False
    
    print(f"\nNilai boolean dari x: {bool_x}")
    print(f"Nilai boolean dari y: {bool_y}")
    print(f"x AND y: {bool_x and bool_y}")
    print(f"x OR y: {bool_x or bool_y}")
    print(f"NOT x: {not bool_x}")
    print(f"x XOR y: {bool_x != bool_y}")  

if __name__ == "__main__":
    main()
