# bagaimana cara copy list di python
# cara copy list di python bisa mengunakan beberapa cara
# mengunakan fungsi copy() pada list
# keuntunagan mengunakan fungsi copy() adalah kita bisa mengcopy list tanpa mengubah nilai list yang asli
# contoh mengunakan fungsi copy()
data_siswa = ["irfan", "budi", "siti", "andi", "cici"]
data_siswa_copy = data_siswa.copy()  # dengan syntax nama variabel.copy()   
print(data_siswa_copy)  # ini akan mengembalikan nilai list yang sudah di copy

# mengunakan slicing pada list
data_nilai = [80, 90, 70, 60, 100]
data_nilai_copy = data_nilai[:]  # dengan syntax nama variabel[:]
print(data_nilai_copy)  # ini akan mengembalikan nilai list yang sudah di copy
# kekurangan mengunakan slicing adalah kita harus menulis ulang nama variabel yang akan di copy