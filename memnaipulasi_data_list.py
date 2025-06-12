# Memanipulasi data pada list
# -Irfan di dalam sebuah bahasa pemograman python kiata bisa mengubah tipe data

# ini sytax untuk memanipulasi data yaitu menambahakan data pada list
print("Berbagai cara menamabahkan data pada list ")
# untu sytax memanipulasi data pada list kita bisa mengunakan kata kunci insert
# sytax insert ini akan menambahkan data pada list pada index yang kita inginkan
data_siswa = ['irfan', 'budi', 'siti']
data_siswa.insert(1,"siti ") # nama variabel .insert(index, value)
print(data_siswa)
# kita juga bisa menambahkan data pada list dengan cara append
data_siswa.append("siti") # nama variabel .append(value)
print(data_siswa) # kekuranagan dari apend adalah kita tidak bisa menentukan indexnya
# kita juga bisa menambahkan data pada list dengan cara extend
data_siswa.extend(["siti", "budi"]) # nama variabel .extend([value1, value2])
print(data_siswa) # extend ini akan menambahkan data pada list dengan cara menambahkan data pada akhir list dan mengabungakan list
# kita juga bisa menambahkan data pada list dengan cara mengunakan operator +       
data_siswa = data_siswa + ["siti", "budi"] # nama variabel = nama variabel + [value1, value2]
print(data_siswa) # ini akan menambahkan data pada list dengan cara menggabungkan dua list
# kita juga bisa menambahkan data pada list dengan cara mengunakan operator *
data_siswa = data_siswa * 2 # nama variabel = nama variabel * 2
print(data_siswa) # ini akan menambahkan data pada list dengan cara mengulangi data pada list sebanyak 2 kali

print("cara merubah data pada list ")

#didalam bahasa pemograman python kita bisa mengubah data pada list dengan cara mengunakan index
data_siswa[0] = "irfan" #dengan syntax nama variabel[index] = value
print(data_siswa) # ini akan mengubah data pada index 0 menjadi irfan


print("cara menghapus data pada list ")
# didalam bahasa pemograman python kita bisa menghapus data pada list dengan cara mengunakan del
del data_siswa[0] # dengan syntax del nama variabel[index]     
print(data_siswa) # ini akan menghapus data pada index 0
# kita juga bisa menghapus data pada list dengan cara mengunakan remove
data_siswa.remove("siti") # dengan syntax nama variabel.remove(value)   
print(data_siswa) # ini akan menghapus data pada list yang bernilai siti
# kita juga bisa menghapus data pada list dengan cara mengunakan pop
data_siswa.pop(0) # dengan syntax nama variabel.pop(index)
print(data_siswa) # ini akan menghapus data pada index 0

# perbedaan menghpus dengan kata kunci del, remove, dan pop
# - del akan menghapus data pada index yang kita inginkan
# - remove akan menghapus data pada list yang bernilai sama dengan value yang kita inginkan
# - pop akan menghapus data pada index yang kita inginkan dan mengembalikan nilai data yang dihapus