import random
import re

# Data item gacha menggunakan data collections - dictionary
# Program ini hanya gacha biasa, tidak ada sistem rate on atau arte off
item_gacha = {
    "5★": ["Chasca", "Lyney", "Diluc", "Keqing", "Mona", "Jean", "Qiqi", "Qiqi", "Qiqi", "Qiqi", "Qiqi"],
    "4★": ["Ororon", "Xiangling", "Charlotte", "Xingqiu", "Fischl", "Sucrose", "Barbara", "Bennett", "Kuki Shinobu"],
    "3★": ["Harbinger of Dawn", "White Tasel", "Thrilling Tales of Dragon Slayers", "Black Tassel", "Debate Club", "Magic Guide", "Emeral Orb", "Sharpshooter's Oath", "Slingshot"]
}

# Inventori player menggunakan dictionary: key (bintang) - value (nama dan jumlah)
inventori = {
    "5★": {},
    "4★": {},
    "3★": {}
}

# Statistik gacha untuk 
statistik = {
    "total pull": 0,
    "5★": 0,
    "4★": 0,
    "3★": 0
}

# Regex untuk username dan password
regex_username = r"^[a-zA-Z0-9]{5,15}$"
regex_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"  # Password hanya huruf besar, kecil, dan angka

# Fungsi untuk melakukan login sebelum melakukan gacha menggunakan function, conditional statement, dan module re
def login():
    print("=== Login untuk Gacha ===")
    while True:
        username = input("Masukkan username (5-15 karakter, hanya huruf dan angka): ")
        password = input("Masukkan password (minimal 8 karakter, huruf besar, huruf kecil, angka): ")

        if not re.match(regex_username, username):
            print("Username tidak valid! Pastikan hanya mengandung huruf dan angka, serta 5-15 karakter.")
            continue

        if not re.match(regex_password, password):
            print("Password tidak valid! Pastikan mengandung minimal 8 karakter, huruf besar, huruf kecil, dan angka.")
            continue
        
        print("Login berhasil!\n")
        break

# Fungsi untuk melakukan gacha
def gacha(jumlah_pull):
    hasil = []
    pity_bintang_4 = 0
    pity_bintang_5 = 0
    
# menggunakan for loop untuk melakukan pull sebanyak input(1/10) kali
    for _ in range(jumlah_pull):
        statistik["total pull"] += 1 #untuk menghitung total pull
        pity_bintang_4 += 1
        pity_bintang_5 += 1

        # Sistem pity
        if pity_bintang_5 == 90: 
            bintang = "5★"
            pity_bintang_5 = 0 #Reset pity bintang 5
        if pity_bintang_4 == 10:
            bintang = "4★"
            pity_bintang_4 = 0 #Reset pity bintang 4
        else:
            # Pull random
            angka_acak = random.random()
            if angka_acak < 0.006: #probabilitas 0.6% untuk 5★
                bintang = "5★"
                pity_bintang_5 = 0 #Reset pity bintang 5
            elif angka_acak < 0.051: #probabilitas 5.7% untuk 4★
                bintang = "4★" 
                pity_bintang_4 = 0 #Reset pity bintang 4
            else: #Sisanya (94.3%) untuk 3★.
                bintang = "3★"

        # Pilih item dari rarity tertentu. Item diambil secara acak dari daftar sesuai rarity (3★, 4★, 5★).
        item = random.choice(item_gacha[bintang])
        hasil.append(f"{bintang} {item}") #menggunakan append ke dict (bintang(key):item(value))

        # Tambahkan ke inventori
        if item not in inventori[bintang]:
            inventori[bintang][item] = 0
        inventori[bintang][item] += 1

        # Perbarui statistik
        statistik[bintang] += 1

    return hasil

# Fungsi untuk menampilkan inventori
def tampilkan_inventori():
    print("\n--- Inventori ---")
    for bintang in inventori:
        print(f"{bintang}:")
        for nama_item in inventori[bintang]:
            jumlah = inventori[bintang][nama_item]
            print(f"  {nama_item} ({jumlah})")
    print()

# Fungsi untuk mencari item di inventori
def cari_item():
    print("\n=== Cari Item di Inventori ===")
    item_cari = input("Masukkan nama item yang ingin dicari: ").strip().lower() #Mmenggunakan string manipulation .lower() untuk mencocokkan input yang berbeda-beda (penggunaan kapital atau tidak)
    ditemukan = False
    for bintang in inventori:
        for nama_item in inventori[bintang]:
            if item_cari in nama_item.lower():
                print(f"Item '{nama_item}' ditemukan di inventori ({bintang}) dengan jumlah {inventori[bintang][nama_item]}.\n")
                ditemukan = True
    if not ditemukan:
        print(f"Item '{item_cari}' tidak ditemukan dalam inventori.\n")

# Fungsi untuk menampilkan statistik gacha
def tampilkan_statistik():
    print("\n--- Statistik Gacha ---")
    print(f"Total Pull: {statistik['total pull']}") #Mengambil data dari dictionary statistik
    print(f"Jumlah 5★: {statistik['5★']}")
    print(f"Jumlah 4★: {statistik['4★']}")
    print(f"Jumlah 3★: {statistik['3★']}")
    print()

# Menu utama
def menu_utama():
    login()  # Panggil fungsi login sebelum menampilkan menu utama

    while True:
        print("=== Simulasi Gacha Genshin Impact ===")
        print("1. Gacha Karakter")
        print("2. Lihat Inventori")
        print("3. Cari Item di Inventori")
        print("4. Lihat Statistik Gacha")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            try:
                pull = int(input("Ingin berapa kali pull? (1/10): "))
                if pull not in [1, 10]:
                    print("Hanya bisa memilih 1 atau 10 pull.")
                    continue
                hasil = gacha(pull)
                print("\n--- Hasil Gacha ---")
                for i in range(len(hasil)):
                    print(hasil[i])
                print()
            except ValueError:
                print("Masukkan angka 1 atau 10.")
        elif pilihan == "2":
            tampilkan_inventori()
        elif pilihan == "3":
            cari_item()
        elif pilihan == "4":
            tampilkan_statistik()
        elif pilihan == "5":
            print("Terima kasih telah mencoba simulasi gacha! Semoga gachamu wangi!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Jalankan program
menu_utama()