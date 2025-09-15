#nested list diguanakan untuk mreprentasikan data yang berelasi atau data yang memiliki hubungan satu sama lain
# Nested list digunakan untuk merepresentasikan struktur data multi-dimensi, seperti matriks (2D array) atau data bertingkat.
# strukur nested list adalah list didalam list

# contoh nested list
data_mahasiswa = [
    ["irfan", "budi", "siti"],
    [80, 90, 70],
    ["A", "B", "C"]
]   
# cara mengakses data pada nested list
print(data_mahasiswa[0][0])  # mengakses data pertama pada list pertama     
print(data_mahasiswa[1][1])  # mengakses data kedua pada list kedua
print(data_mahasiswa[2][2])  # mengakses data ketiga pada list ketiga
# cara mengakses data pada nested list dengan perulangan

# contoh pengugunaan nested list pada vektor mahasiswa
matriks_mahasiswa = [
    ["Nama", "Nilai", "Kelas"],
    ["Irfan", 80, "A"],
    ["Budi", 90, "B"],
    ["Siti", 70, "C"]
]       
for index, mahasiswa in enumerate(matriks_mahasiswa) :
      # mencetak data dengan spasi
      print(index)
      print(mahasiswa)  # mencetak baris baru setelah setiap list

"""Kapan Nested List Berguna?
Saat mengolah tabel data

Saat membuat matriks

Untuk representasi struktur hierarki (misalnya: menu, pohon keluarga, dsb.)"""







#oot
for mahasiswa in data_mahasiswa:
    for data in mahasiswa:
        print(data, end=" ")  # mencetak data dengan spasi
    print()  # mencetak baris baru setelah setiap list

# cara mengakses data pada nested list dengan perulangan dan indeks
for i in range(len(data_mahasiswa)):
    for j in range(len(data_mahasiswa[i])):
        print(data_mahasiswa[i][j], end=" ")  # mencetak data dengan spasi
    print()  # mencetak baris baru setelah setiap list