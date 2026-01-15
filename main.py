# ==========================
# Import Data dan Fungsi
# ==========================

# Import daftar nasabah dari file data.py
# diasumsikan nasabah_list adalah list of dict yang berisi data akun
from data import nasabah_list

# Import semua fungsi ATM dari file atm.py
# termasuk: login, cek_saldo, tarik_tunai, setor_tunai, ganti_pin, tampilkan_riwayat
from atm import *


# ==========================
# Fungsi Menu Utama
# ==========================

def menu():
    # Menampilkan menu utama ATM
    print("\n=== MENU ATM ===")  # \n untuk baris baru agar tampilan rapi
    print("1. Login")           # Opsi untuk login ke akun
    print("2. Tambah Nasabah")  # Opsi untuk membuat akun baru
    print("3. Hapus Nasabah")   # Opsi untuk menghapus akun
    print("0. Keluar")          # Opsi untuk keluar dari program


# ==========================
# Fungsi Menu Setelah Login
# ==========================

def menu_akun(akun):
    # Menampilkan menu khusus setelah user login
    print("\n=== MENU AKUN ===")       # Judul menu akun
    print("1. Cek Saldo")              # Melihat saldo
    print("2. Tarik Tunai")            # Mengurangi saldo
    print("3. Setor Tunai")            # Menambah saldo
    print("4. Ganti PIN")              # Mengubah PIN akun
    print("5. Riwayat Transaksi")      # Melihat histori transaksi
    print("0. Logout")                 # Keluar dari akun


# ==========================
# Loop Utama Program
# ==========================

while True:
    menu()  # Tampilkan menu utama
    pilihan = input("Pilih menu: ")  # Ambil input user sebagai string

    if pilihan == "1":
        # Jika user memilih login
        akun = login(nasabah_list)  # Panggil fungsi login, return dict akun jika berhasil

        if akun:
            # Jika login berhasil (akun tidak None), masuk ke loop menu akun
            while True:
                menu_akun(akun)  # Tampilkan menu akun
                aksi = input("Pilih aksi: ")  # Ambil input aksi dari user

                # Cek aksi yang dipilih dan panggil fungsi sesuai
                if aksi == "1":
                    cek_saldo(akun)
                elif aksi == "2":
                    tarik_tunai(akun)
                elif aksi == "3":
                    setor_tunai(akun)
                elif aksi == "4":
                    ganti_pin(akun)
                elif aksi == "5":
                    tampilkan_riwayat(akun)
                elif aksi == "0":
                    print("Logout berhasil.")
                    break  # Keluar dari loop akun, kembali ke menu utama
                else:
                    print("Pilihan tidak valid.")

    elif pilihan == "2":
        # Tambah nasabah baru
        tambah_nasabah(nasabah_list)

    elif pilihan == "3":
        # Hapus nasabah
        hapus_nasabah(nasabah_list)

    elif pilihan == "0":
        # Keluar dari program
        print("Terima kasih telah menggunakan ATM AJI.")
        break

    else:
        # Jika input tidak dikenali
        print("Pilihan tidak valid.")