# Berkas: praktik/utilitas_matematika.py

def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return 0.5 * a * t

def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def tampilkan_menu():
    print("\n--- APLIKASI UTILITAS MATEMATIKA ---")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))
            print("Luas =", luas_persegi_panjang(p, l))
            
        elif pilihan == "2":
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))
            print("Luas =", luas_segitiga(a, t))
            
        elif pilihan == "3":
            n = int(input("Masukkan nilai n: "))
            if n >= 0:
                print("Jumlah =", jumlah_n(n))
            else:
                print("n harus nonnegatif")
                
        elif pilihan == "4":
            n = int(input("Masukkan nilai n: "))
            if n >= 0:
                print("Faktorial =", faktorial(n))
            else:
                print("n harus nonnegatif")
                
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()