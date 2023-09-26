import time

def clear_screen():
    print("\033c", end="")
    
def display_menu():
    clear_screen()
    print("Kalkulator Sederhana")
    print("--------------------")
    print("Pilih Operasi : ")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y 

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Tidak Bisa Membagi Dengan Nol"
    return x / y

while True:
    display_menu()
    pilihan = input("Masukan Nomor Operasi (1/2/3/4/5):")
    
    if pilihan == '5':
        print("Keluar dari kalkulator")
        break
    
    if pilihan not in ('1', '2', '3', '4'):
        input("Pilihan tidak valid, Tekan ENTER untuk melanjutkan")
        continue
    
    angka1 = float(input("Masukan angka pertama:"))
    angka2 = float(input("Masukan angka kedua:"))
    
    if pilihan  == '1':
        hasil = tambah(angka1, angka2)
        print(f"Hasil:{angka1}+{angka2}={hasil}")
    elif pilihan  == '2':
        hasil = kurang(angka1, angka2)
        print(f"Hasil:{angka1}-{angka2}={hasil}")
    elif pilihan  == '3':
        hasil = kali(angka1, angka2)
        print(f"Hasil:{angka1}*{angka2}={hasil}")
    elif pilihan  == '4':
        hasil = bagi(angka1, angka2)
        print(f"Hasil:{angka1}/{angka2}={hasil}")
        
    input("Tekan Enter Untuk Melanjutkan.....")
