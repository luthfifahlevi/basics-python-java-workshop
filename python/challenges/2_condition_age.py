# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
name = input("Masukan nama Anda: ").strip()
age = input("Masukan usia Anda: ").strip()
# 2. TODO Tentukan kategori berdasarkan usia
if age.isdigit():
    age = int(age)
    if age < 12:
        category = "Anak-anak"
    elif age < 18:
        category = "Remaja"
    elif age < 60:
        category = "Dewasa"
    else:
        category = "Lansia"
else:
    category = "Invalid"
# 3. TODO: Cetak kategori
print(f"Halo {name}, Anda dikategorikan sebagai: {category}")
