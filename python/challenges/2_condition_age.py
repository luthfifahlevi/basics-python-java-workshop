# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
usia = int(input("Masukkan usia Anda : "))

# 2. TODO Tentukan kategori berdasarkan usia
kat = "lansia"
if usia < 12:
    kat = "anak-anak"
elif usia <= 17:
    kat = "remaja"
elif usia <= 59:
    kat = "dewasa"

print(kat)