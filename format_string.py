#Format string dalam bahasa Python adalah teknik yang digunakan untuk menggabungkan variabel atau nilai dengan teks, 
# memungkinkan pembuatan string yang lebih dinamis dan mudah dibaca.
#  Ada beberapa metode untuk melakukan format string, masing-masing dengan sintaks dan kegunaan yang berbeda.

# Operator %
# Operator % dalam bahasa pemrograman Python adalah metode untuk melakukan format string,
#  yang dikenal sebagai string-formatting operator. 
# Metode ini memungkinkan penggabungan variabel atau nilai ke dalam string dengan menggunakan placeholder yang ditandai dengan simbol %. 
# Ini adalah salah satu cara tertua untuk melakukan format string di Python, mirip dengan fungsi printf di bahasa C.

# Operator % menggunakan format specifiers untuk menunjukkan jenis data yang akan disisipkan ke dalam string. Beberapa format specifiers yang umum digunakan meliputi:
# %s: untuk menyisipkan string.
# %d: untuk menyisipkan bilangan bulat (integer).
# %f: untuk menyisipkan bilangan pecahan (float).
# %x: untuk menyisipkan bilangan dalam format heksadesimal.
# %b: untuk menyisipkan bilangan dalam format biner.

#contoh 

Nama = "Irfan"
No_absen = 21
Biodata = "Ini adalah biodataku Nama %s No absen %d" % (Nama, No_absen) # ya ini mirip kaya string iterpolation di flutter ouput  kode ini adalah Ini adalah biodataku Nama Irfan No absen 21
print(Biodata)

#metode format() di stirng adalah metode yang digunakan untuk melakukan format string dengan menyisipkan variabel atau nilai ke dalam string.
#  Metode ini memungkinkan penggabungan string dengan menggunakan placeholder yang ditandai dengan kurung kurawal {}.

#contoh 
Nama = "Irfan" 
No_absen = 21
Biodata = "Ini adalah biodataku Nama {} No absen {}".format(Nama, No_absen)  #ouput dari kode ini adalah = Ini adalah biodataku Nama Irfan No absen 21
print(Biodata)

#f string di bahasa pemogrman python adalah metode yang digunakan untuk melakukan format string dengan menyisipkan variabel atau nilai ke dalam string.
#  Metode ini memungkinkan penggabungan string dengan menggunakan placeholder yang ditandai dengan kurung kurawal {}.
# f string memungkinkan penggunaan variabel langsung di dalam string, tanpa perlu menggunakan metode format() atau operator %.
# f string ditandai dengan awalan huruf f sebelum string, diikuti dengan string yang akan diformat.
# Variabel atau nilai yang akan disisipkan ke dalam string diletakkan di dalam placeholder yang ditandai dengan kurung kurawal {}.
# contoh
Nama = "Irfan"
No_absen = 21
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen}" #output dari kode ini adalah = Ini adalah biodataku Nama Irfan No absen 21
print(Biodata)

# kita dapat menamabahka :d setelah variabel untuk menentukan tipe data yang akan di tampilkan memebuat bilangan tersebt menjadi bilangan bulat
#contoh
umur = 21
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen} Umur {umur:d}" #output = 21
print(Biodata)

# kita dapat menambahkan :.2f setelah variabel untuk menentukan tipe data yang akan di tampilkan memebuat bilangan tersebt menjadi bilangan pecahan
# siyntax :{variabel:.2f}
#contoh
nilai = 90.521
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen} Nilai {nilai:.2f}" #output = 90.52
print(Biodata)

# kita bisa menambakahkan :, setelah {variabel} untuk menambahkan pemisah ribuan    
#contoh
uang = 10000000000000
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen} Uang {uang:,}"# output = 10,000,000,000,000
print(Biodata)

#kita bisa menambahkan  ledding zero set di dalam bahasa pemograman python untuk menambahkan angka 0 di depan angka
# untuk symtaxnya {variabel:02d} jika bentuknya pecahan atau float {variabel:02f}
#contoh untuk bilangan bulat
umur = 21
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen} Umur {umur:010d}" #output = 21
print(Biodata)

#contoh untuk bilangan pecahan
nilai = 90.521
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen} Nilai {nilai:010.2f}" #output = 90.52

# di dalama bahasa python kit bisa menapilkan tanda minus dapan plus di depan angka cara menambahkannya adalah dengan menambahkan simbol + atau - setelah : 
# untuk sytaxnya {variabel:+d} jika bentuknya pecahan atau float {variabel:+f}
#contoh 

uang = -1023.23552
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen} Uang {uang:+.2f}" #output = -1023.24
print(Biodata)
 

 # didalam bahsa pemograman python kita bisa memformat persen dengan  cara dengan cara menambahkan %% setelah variabel
 #contoh 
persen = 0.85
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen} Persen {persen:.2%}" #output = 85.00%
print(Biodata)

# didalama bahasa pemograman python kita bisa melakukan operasi aritmatika di dalama kurung kurungkurwal {}
#contoh
a = 12 
b = 3
jumlah = f"{a} + {b} = {a+b}" #output = 12 + 3 = 15
print(jumlah)

# didalam bahasa pemograman python juga ada formata binary, octal, dan hexadesimal
#contoh pemgunaan setip format tersebut 
angka = 255 
print(f"Binary : {angka:b}") #output = 11111111 
print(f"Octal : {angka:o}") #output = 377
print(f"Hexadesimal : {angka:x}") #output = ff  
#contoh penggabungan    
print(f"Binary : {angka:b} Octal : {angka:o} Hexadesimal : {angka:x}") #output = Binary : 11111111 Octal : 377 Hexades
