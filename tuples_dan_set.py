#data tuples adalah struktur data yang tidak dapat diubah (immutable) dan digunakan untuk menyimpan beberapa item dalam satu variabel.
# Data set adalah struktur data yang digunakan untuk menyimpan beberapa item unik dalam satu variabel.
#dapat diindeks, tetapi tidak dapat diubah.

# Contoh penggunaan tuples
my_tuple = (1, "makan bakso", 2.4, 4, 5) # datanya bisa berupa campuran tipe data
# Tuples dapat berisi berbagai tipe data, termasuk integer, string, dan float.
print("Contoh penggunaan tuples:")
print("Isi tuple:", my_tuple)

#sedangkan set tidak dapat berisi item yang sama, jika kita mencoba menambahkan item yang sama, maka akan diabaikan
my_set = {1, "makan bakso", 2.4, 4, 5, 1} # set tidak mengizinkan duplikasi
# Set hanya menyimpan item unik, jadi item yang sama tidak akan ditambahkan lagi.
print("Contoh penggunaan set:") # tidak terindeks jadi set seperti himpunan matematika. urutan matematika
print("Isi set:", my_set)

#jika kita ingin mengakses item di data set, kiba bisa mengakasesnya tetapi aotputnya akan acak
# karena set tidak memiliki urutan yang tetap.
# Jadi, kita tidak bisa mengakses item dengan indeks seperti pada list atau tuple.  
# Namun, kita bisa mengubah set menjadi list jika kita ingin mengakses item dengan indeks.
my_set_list = list(my_set)  # Mengubah set menjadi list untuk mengakses item    