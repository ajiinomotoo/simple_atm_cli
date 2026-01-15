# ==========================
# Import Bagian-Bagian yang Dibutuhkan
# ==========================

# Import fungsi helper dari utils.py:
# - input_angka → memastikan input berupa angka (integer)
# - input_pin   → memastikan PIN valid (4 digit angka)
# - format_rupiah → mengubah angka jadi format uang Indonesia (Rp50.000)
from utils import input_angka, input_pin, format_rupiah

# Import Fore dan Style dari colorama untuk memberi warna pada teks output
# Fore = warna teks (misalnya Fore.RED, Fore.GREEN)
# Style.RESET_ALL = mengembalikan warna ke default setelah print
from colorama import Fore, Style

# Import datetime untuk menambahkan timestamp (tanggal & jam) di riwayat transaksi
from datetime import datetime




# ==========================
# Fungsi Menu Akun
# ==========================

# ==========================
# Fungsi LOGIN
# ==========================
def login(nasabah_list):
    pin = input("Masukkan PIN: ")  # Ambil input PIN dari user
    for akun in nasabah_list:  # Loop setiap akun dalam list nasabah
        if akun["PIN"] == pin:  # Cek apakah PIN cocok
            print("Login berhasil.")  # Beri pesan sukses
            return akun  # Return dict akun yang cocok
    print("PIN salah.")  # Jika tidak ada yang cocok
    return None  # Return None → login gagal


# ==========================
# Fungsi CEK SALDO
# ==========================
# Fungsi cek_saldo → menampilkan saldo akun dengan format rupiah
def cek_saldo(akun):
    # akun adalah dictionary dengan key "Saldo"
    # format_rupiah dipakai agar angka lebih mudah dibaca (Rp50.000 bukan Rp50000)
    print(Fore.CYAN + f"Saldo Anda: {format_rupiah(akun['Saldo'])}" + Style.RESET_ALL)
  # f-string untuk menampilkan saldo akun


# ==========================
# Fungsi TARIK TUNAI
# ==========================
def tarik_tunai(akun):
    # Ambil input jumlah tarik, validasi dengan input_angka
    jumlah = input_angka("Jumlah tarik: Rp")

    # Validasi: jumlah harus lebih dari 0
    if jumlah <= 0:
        print(Fore.YELLOW + "Jumlah harus lebih dari Rp0." + Style.RESET_ALL)
        return  # keluar dari fungsi tanpa melakukan transaksi

    # Validasi: cek apakah saldo cukup
    if jumlah <= akun["Saldo"]:
        # Kurangi saldo
        akun["Saldo"] -= jumlah

        # Buat timestamp transaksi (contoh: 2026-01-08 16:45)
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Simpan riwayat transaksi ke list akun["Riwayat"]
        # format_rupiah dipakai agar jumlah tampil rapi
        akun["Riwayat"].append(f"[{waktu}] Tarik {format_rupiah(jumlah)}")

        # Tampilkan pesan sukses + saldo terbaru
        print(Fore.GREEN + "Transaksi berhasil ✅" + Style.RESET_ALL)
        print(Fore.CYAN + f"Saldo Anda sekarang: {format_rupiah(akun['Saldo'])}" + Style.RESET_ALL)
    else:
        # Jika saldo tidak cukup
        print(Fore.RED + "Saldo tidak cukup ❌" + Style.RESET_ALL)


# ==========================
# Fungsi SETOR TUNAI
# ==========================
def setor_tunai(akun):
    # Ambil input jumlah setor
    jumlah = input_angka("Jumlah setor: Rp")

    # Validasi: jumlah harus lebih dari 0
    if jumlah <= 0:
        print(Fore.YELLOW + "Jumlah harus lebih dari Rp0." + Style.RESET_ALL)
        return

    # Tambahkan saldo
    akun["Saldo"] += jumlah

    # Buat timestamp transaksi
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Simpan riwayat transaksi
    akun["Riwayat"].append(f"[{waktu}] Setor {format_rupiah(jumlah)}")

    # Tampilkan pesan sukses + saldo terbaru
    print(Fore.GREEN + f"Setoran berhasil ✅. Saldo Anda sekarang: {format_rupiah(akun['Saldo'])}" + Style.RESET_ALL)



# ==========================
# Fungsi GANTI PIN
# ==========================
def ganti_pin(akun):
    pin_baru = input_pin(
        "Masukkan PIN baru: ")  # Ambil PIN baru dengan validasi helper
    if pin_baru is None:  # Jika None → input tidak valid
        return
    if pin_baru == akun["PIN"]:  # Cek agar PIN baru tidak sama dengan lama
        print(Fore.RED + "PIN tidak valid atau sama dengan PIN lama." + Style.RESET_ALL)
        return
    akun["PIN"] = pin_baru  # Update field PIN
    akun["Riwayat"].append("Ganti PIN")  # Catat aksi ganti PIN ke riwayat
    print(Fore.GREEN + "PIN berhasil diganti." + Style.RESET_ALL)


# ==========================
# Fungsi TAMPILKAN RIWAYAT
# ==========================
def tampilkan_riwayat(akun):
    print(Fore.MAGENTA + "\n=== Riwayat Transaksi ===" + Style.RESET_ALL)
    if not akun["Riwayat"]:  # Cek apakah list riwayat kosong
        print("- Belum ada transaksi.")
        return
    for r in akun["Riwayat"]:  # Loop setiap item riwayat
        print("-", r)


# ==========================
# Fungsi TAMBAH NASABAH (Create)
# ==========================
def tambah_nasabah(nasabah_list):
    pin = input_pin("PIN baru (4 digit): ")  # Ambil PIN baru dengan validasi
    if pin is None:  # Jika None → input tidak valid
        return
    for akun in nasabah_list:  # Loop untuk cek duplikasi PIN
        if akun["PIN"] == pin:
            print("PIN sudah digunakan. Pilih PIN lain.")
            return
    saldo = input_angka(
        "Saldo awal: Rp")  # Ambil saldo awal dengan validasi angka
    if saldo < 0:  # Validasi saldo tidak negatif
        print("Saldo awal tidak boleh negatif.")
        return
    nasabah_baru = {  # Buat dict akun baru
        "PIN": pin,
        "Saldo": saldo,
        "Riwayat": []
    }
    nasabah_list.append(nasabah_baru)  # Tambahkan dict ke list nasabah
    print("Nasabah baru ditambahkan.")


# ==========================
# Fungsi HAPUS NASABAH (Delete)
# ==========================
def hapus_nasabah(nasabah_list):
    pin = input("PIN akun yang akan dihapus: ")  # Ambil PIN target
    for idx, akun in enumerate(nasabah_list):  # Loop dengan indeks
        if akun["PIN"] == pin:  # Jika PIN cocok
            del nasabah_list[idx]  # Hapus akun dari list
            print("Akun berhasil dihapus.")
            return
    print("Akun tidak ditemukan.")  # Pesan jika PIN tidak ada
