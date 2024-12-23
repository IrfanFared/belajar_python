#merubah semua huruf menjadi huruf kapital atau uppercase
nama = "irfan pratama"
uppercase_nama = nama.upper()
print(uppercase_nama)

#merubah semua huruf menjadi huruf tidak kapital atau lower case
lowercase_nama = nama.lower()
print(lowercase_nama)

#contoh pengecekan apakah sebuah string lower case atau tidak dengan mengunakan is
pengecekan_lowercase = nama.islower()
print(pengecekan_lowercase)

#di dalam bahasa pemogran bahasa pyton kita bisa mengecek string berisi huruf atau angka

mengencek_string_huruf = nama.isalpha()
print("mengecek apakah semuanya huruf"+ str(mengencek_string_huruf))

alamat = "rt8"
mengencek_string_hurufdanaangka = alamat.isalnum()
print(mengencek_string_hurufdanaangka)

#isalnum: Mengembalikan True jika string hanya berisi huruf dan angka (alphanumeric), tanpa spasi atau karakter khusus.
#isalpha: Mengembalikan True jika string hanya berisi huruf.
#isascii: Mengembalikan True jika string hanya berisi karakter ASCII.
#isdecimal: Mengembalikan True jika string hanya berisi angka desimal.
#isdigit: Mengembalikan True jika string hanya berisi digit (0–9).
#isidentifier: Mengembalikan True jika string adalah nama variabel yang valid.
#islower: Mengembalikan True jika semua huruf dalam string adalah huruf kecil.
#isnumeric: Mengembalikan True jika string hanya berisi angka (termasuk Unicode angka seperti pecahan atau angka romawi).
#isprintable: Mengembalikan True jika semua karakter dalam string dapat dicetak.
#isspace: Mengembalikan True jika string hanya berisi spasi putih (space, tab, newline, dll.).
#istitle: Mengembalikan True jika string dalam format title case (setiap kata diawali huruf besar).
#isupper: Mengembalikan True jika semua huruf dalam string adalah huruf besar.

#didalam bahasa pemograman python kita bisa mengecek apakah sebuah string diawali dengan kata x dan diakhiri dengan kata y
# dengan mengunakan method startswith() dann endswith

nama_lengkap = "Irfan Pratama".startswith("Irfan")
print(nama_lengkap)
nama_lengkap_p = "Irfan Pratamax".endswith("Pratamax")
print(nama_lengkap_p)