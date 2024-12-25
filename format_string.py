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
Biodata = "Ini adalah biodataku Nama %s No absen %d" % (Nama, No_absen) # ya ini mirip kaya string iterpolation di flutter
print(Biodata)

#metode format() di stirng adalah metode yang digunakan untuk melakukan format string dengan menyisipkan variabel atau nilai ke dalam string.
#  Metode ini memungkinkan penggabungan string dengan menggunakan placeholder yang ditandai dengan kurung kurawal {}.

#contoh 
Nama = "Irfan" 
No_absen = 21
Biodata = "Ini adalah biodataku Nama {} No absen {}".format(Nama, No_absen) 
print(Biodata)

#f string di bahasa pemogrman python adalah metode yang digunakan untuk melakukan format string dengan menyisipkan variabel atau nilai ke dalam string.
#  Metode ini memungkinkan penggabungan string dengan menggunakan placeholder yang ditandai dengan kurung kurawal {}.
# f string memungkinkan penggunaan variabel langsung di dalam string, tanpa perlu menggunakan metode format() atau operator %.
# f string ditandai dengan awalan huruf f sebelum string, diikuti dengan string yang akan diformat.
# Variabel atau nilai yang akan disisipkan ke dalam string diletakkan di dalam placeholder yang ditandai dengan kurung kurawal {}.
# contoh
Nama = "Irfan"
No_absen = 21
Biodata = f"Ini adalah biodataku Nama {Nama} No absen {No_absen}"
print(Biodata)
