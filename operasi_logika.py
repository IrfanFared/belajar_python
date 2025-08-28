#didalam bahasa pemogrman bahasa pyton ada yang namanya  operasi logika digunakan untuk membandingkan  nilai atau menentukan  kondi dalam progam

a = True
b = False
#mengembalikan nilai true jika  kedua kondisi true
#jika salah satu  false  hasilnya false 
print(a and b,"ini namanya logika dan ")

#mengembalikan nilai true jika salah satu bernilai tru
#mengembalikan nilai false hanya jika  kedua kondisi bernilai false 
a = True
b = False
print(a or b,"ini namanya logika atau")

a = True
b = False
#memblikan nilai  logika. jika nilai variabel true maka akan di kembalikan menjadi false
print(not a)
print(not b,"ini namanya operasi logika tidak")

#contoh gabungan operator logika 

a = 10
b = 12
lulus_ujian = a >= 10 and b >= 10
print("selamat anda lulus ujian",lulus_ujian)
tidak_lulus_ujian = a > 8 or b < 13
print(tidak_lulus_ujian)


