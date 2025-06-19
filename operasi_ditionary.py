# didalam pyton terdapat beberapa fungsi yang dapat digunakan untuk mengelola dictionary, seperti:
# kita bisa mehiting jumlah item dalam dictionary menggunakan fungsi len()
#contoh penggunaan fungsi len()
nama_anak = {
    "anak " : "budi",
    "umur" : 10,
}

lendik = len(nama_anak)  # Menghitung jumlah item dalam dictionary
print(f"Jumlah item dalam dictionary: {lendik}")

# key sama seperti index hanya saja key diigunakan untuk mengaskes nilai dalam dictionary.
# kita bisa mengecek apakah sebuaha variabel adalah key atau tidak dengan menggunakan operator in

key = "anak "
cek_key = key in nama_anak  # Mengecek apakah key ada dalam dictionary
print(f"Apakah '{key}' adalah key dalam dictionary? {cek_key}")

# get adalah fungsi yang digunakan untuk mengakses nilai dalam dictionary berdasarkan key.
nilai = nama_anak.get("anak ")  # Mengakses nilai berdasarkan key
print(f"Nilai untuk key '{key}': {nilai}")


# cara mengupada data di dictionary adalah dengan menggunakan key yang ingin diubah.

# Mengubah nilai dalam dictionary
nama_anak["umur"] = "usia"  # Mengubah nilai berdasarkan key
print(f"Nilai setelah diubah untuk key 'umur': {nama_anak['umur']}")

#kita juga bisa menambahkan item baru ke dalam dictionary dengan cara yang sama seperti mengubah nilai.
# Menambahkan item baru ke dalam dictionary
nama_anak["alamat"] = "Jakarta"  # Menambahkan item baru        
print(f"Item baru ditambahkan: {nama_anak['alamat']}")

#kata kuci update digunakan untuk mengubah nilai dalam dictionary.
# Menggunakan metode update untuk mengubah nilai dalam dictionary
# kata kunci update
# akan menambah nilai baru jika key tidak ada,atau mengubah nilai jika key sudah ada
nama_anak.update({"umur": 12})  # Mengubah nilai berdasarkan key
print(f"Nilai setelah update untuk key 'umur': {nama_anak['umur']}")

# kita juga bisa menghapus item dari dictionary menggunakan fungsi del atau pop.
# Menghapus item dari dictionary menggunakan del
del nama_anak["alamat"]  # Menghapus item berdasarkan key
print(f"Item 'alamat' setelah dihapus: {nama_anak}")
# Menghapus item dari dictionary menggunakan pop
nilai_hapus = nama_anak.pop("umur")  # Menghapus item berdasarkan key dan

