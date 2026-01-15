# ==========================
# DATA NASABAH
# ==========================

# List berisi dictionary → sesuai ketentuan "List of Dict"
# Setiap dictionary merepresentasikan satu akun nasabah ATM
nasabah_list = [
    {
        "PIN": "1234",  # Field PIN: string 4 digit sebagai identitas login
        "Saldo": 500000,  # Field Saldo: integer, menyimpan jumlah uang nasabah
        "Riwayat":
        []  # Field Riwayat: list kosong, akan diisi catatan transaksi
    },
    {
        "PIN": "5678",  # Akun kedua dengan PIN berbeda
        "Saldo": 250000,  # Saldo awal nasabah kedua
        "Riwayat": []  # Riwayat transaksi kosong, akan bertambah saat ada aksi
    }
]

# Catatan:
# - Struktur ini bisa ditambah/dihapus lewat fungsi CRUD di atm.py
# - Dengan format List of Dict, kita bisa menyimpan banyak akun sekaligus
# - Field 'Riwayat' akan diisi string seperti "Setor Rp50000" atau "Tarik Rp100000"
