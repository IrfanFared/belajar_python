# ketika sebuah fungsi mengembalikan nilai, kita bisa menggunakan keyword return
#maka nilai tersebut akan dikembalikan ke pemanggil fungsi
# dan bisa disimpan dalam variabel
def jumlah(n1, n2):
    total = n1 + n2
    return total
# contoh pemanggilan fungsi
hasil = jumlah(10, 20)
print("Hasil penjumlahan:", hasil)

#retur diguanakan unuk mengahiri sebuah fungsi 
def fungsi_akhir():
    print("irfan ganteng")
    return ("irfan suka matha")# akhir dari sebuah fungsi
    print("fungsi ini tidak akan di jalankan") # kode ini akan tidak dijalankan karena bari sebulnya ada keyword retur
