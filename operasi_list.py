# didalam bahasa pemmograman python kita bisa mengurutkan data dengan
# cara mengunakan fungsi sorted dimana fungsi sorted ini akan mengembalikan nilai list yang sudah diurutkan
# dan tidak mengubah nilai list yang asli
data_siswa = ["irfan", "budi", "siti", "andi", "cici"]
data_siswa_urut = sorted(data_siswa) # dengan syntax sorted(nama variabel) dan ouput
print(data_siswa_urut) # ini akan mengembalikan nilai list yang sudah diurutkan


# short di  tipe data angka di list akan mengurukan angka pada list dari terbesar ke terkecil
data_nilai = [80, 90, 70, 60, 100]
data_nilai_urut = sorted(data_nilai) # dengan syntax sorted(nama variabel, reverse=True)
print(data_nilai_urut) # ini akan mengembalikan nilai list yang sudah diurutkan dari terbesar ke terkecil


# cara mengabil indeks pada list
data_siswa = ["irfan", "budi", "siti", "andi", "cici"]  
indeks_siswa = data_siswa.index("siti") # dengan syntax nama variabel.index(value)
print(indeks_siswa) # ini akan mengembalikan nilai index dari data yang kita cari   

# reverse pada list berguna untuk membalikan urutan pada list dengan contoh 
data_siswa.reverse() # dengan syntax nama variabel.reverse()
print(data_siswa) # ini akan membalikan urutan pada list        

# berlaku pada list dengan tipe data int, float, dan string
# kita bisa mengunakan kata kunci reversed untuk membalikan urutan pada list
data_nilai = [80, 90, 70, 60, 100]
data_nilai_reversed = list(reversed(data_nilai)) # dengan syntax list(reversed(nama variabel))
print(data_nilai_reversed) # ini akan membalikan urutan pada list
# kata kunci reversed bisa mengunakan true atau false
# untuk mengurutkan data pada list
data_nilai_urut = sorted(data_nilai, reverse=True) # dengan syntax sorted(nama variabel, reverse=True)
print(data_nilai_urut) # ini akan mengembalikan nilai list yang sudah diurutkan dari terbesar ke terkecil   

