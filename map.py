"""
map pada python adalah sebuah fungsi yang digunakan untuk menerapkan sebuah fungsi ke setiap item dari iterable (seperti list atau tuple) dan mengembalikan hasilnya sebagai sebuah map object.
 Map object dapat diubah menjadi list atau tipe data lainnya jika diperlukan.

 sytasis map adalah sebagai berikut:
map(fungsi, iterable)

"""

#contoh pengunaan map

angka = [1,2,3,4,5,6,7,8,9]

fungsi_kuadrat = map(lambda x : x*x,angka)

print(list(fungsi_kuadrat)) #hasil akhir bisa di akses dengan mengkorversi objek ke tipa data lain misalnya list
