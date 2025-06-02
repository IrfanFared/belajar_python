# di dalama bahaa python kita bisa memnipulasi string 
# sting concatenate contoh

nama_depan = "Muhammad Irfan"
nama_belakang="pratama"

nama_lengkap = nama_depan + "" + nama_belakang #kamu bisa menambakan spass bisa gunakan string kosong
print(nama_lengkap)

# didalam python kita bisa mengitung ada berapa panjang string string
#semua string termasung spasi dihitung sebagai karakter
#contoh

panjang_string = len(nama_lengkap)
print(panjang_string)

#di dalam bahasa pemograman python kita bisa mengecek char atau string berasa di string atau tidak 
#contoh

string_i = "I"
cek_status_apakah_string_i_ada_di_variabelnamalengkap = string_i in nama_lengkap
print(cek_status_apakah_string_i_ada_di_variabelnamalengkap)

#negasi
string_x = "x"
cek_status_apakah_string_x_tidak_ada_di_variabelnamalengkap = string_i not in nama_lengkap
print(cek_status_apakah_string_x_tidak_ada_di_variabelnamalengkap)
 
#mengulang string yang sama
print("Violet istrinya Irfan\n"*2) #\n untuk membuat baris baru
#Menggunakan metode format untuk menyisipkan nilai ke dalam string

#indexing
indexing = "index 2" "  "+ nama_lengkap[2] #kalo ini dimulai dari angka 0
indexing_jika_mines = "index -2" "  "+ nama_lengkap[-2] #jika mines dimulai dari belakan
indexing_dari_n_ke_n = "index dari 0 samapi 6" "  " +nama_lengkap[0:6] # di python titik 2 arti "sampai"

print(indexing_jika_mines)
print(indexing)
print(indexing_dari_n_ke_n)

indexing_dengan_jeda = nama_lengkap[1:3:5]
print(indexing_dengan_jeda)

#Fungsi ASCII dalam pemrograman Python merujuk pada penggunaan kode American Standard Code for Information Interchange, 
#yang merupakan standar untuk mewakili karakter dalam bentuk numerik. 
# Dalam konteks Python, ada fungsi bawaan yang disebut ascii(), yang berfungsi untuk mengonversi objek menjadi representasi string yang hanya mengandung karakter ASCII, menggantikan karakter non-ASCII dengan urutan escape.
ascii_code = ord("A")  # Fungsi ord() mengembalikan nilai kode ASCII dari karakter "I"
print(str(ascii_code)) # Fungsi str() mengubah nilai numerik menjadi string, kemudian mencetaknya

#operator dalam bentuk method

nama_istri_Irfan = "violet Claudia Clasrisa"
menghitung_jumlah_charakter_O = nama_istri_Irfan.count("a")
print(str(menghitung_jumlah_charakter_O))
