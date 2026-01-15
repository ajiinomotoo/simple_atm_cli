# ==========================
# Fungsi Helper untuk Validasi Input
# ==========================


# Fungsi input_angka memastikan user memasukkan angka (integer)
def input_angka(prompt):
    while True:  # Loop terus sampai input valid
        try:
            nilai = int(input(prompt))  # Coba konversi input ke integer
            return nilai  # Jika berhasil, return nilai
        except ValueError:  # Jika gagal (misal input huruf)
            print("Input harus berupa angka!")  # Pesan error, lalu loop ulang


# Fungsi input_pin memastikan PIN berupa 4 digit angka
def input_pin(prompt):
    pin = input(prompt)  # Ambil input PIN sebagai string
    if pin.isdigit() and len(
            pin) == 4:  # Cek apakah semua karakter angka dan panjang 4 digit
        return pin  # Jika valid, return PIN
    else:
        print("PIN harus 4 digit angka.")  # Pesan error jika tidak valid
        return None  # Return None → menandakan input gagal
    

# Fungsi untuk format angka jadi Rupiah dengan pemisah ribuan
def format_rupiah(angka):
    return f"Rp{angka:,}".replace(",", ".")
    # f-string dengan :, menambahkan koma sebagai pemisah ribuan
    # lalu replace koma jadi titik agar sesuai format Indonesia
