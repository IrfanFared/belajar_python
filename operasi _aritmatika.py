a = int(input("masukan nilai anda =")) #hasil dari input di di pyton defaultnya adalah string jika kita ingin menjadikan sebuah nilai iyu int
b = int(input("masukan nilai anda =")) # maka kita harus ubah dulu atau casting 

nilai_penjumlahan = a + b
nilai_pemgurangan = a - b
nilai_perkalian = a * b
nilai_pembagiam = a / b
nilai_eksponen = a ** b 
nilai_pembagian_sisa= a % b #nilai modulus 
nilai_hasil_pembulatan_pembagian = a // b #flor division 

print(nilai_penjumlahan)
print(nilai_pemgurangan)
print(nilai_perkalian)
print(nilai_pembagiam)




#Operator Precedence (prioritas operator) di Python adalah aturan yang menentukan urutan evaluasi operator dalam suatu ekspresi. Ketika sebuah ekspresi memiliki beberapa operator, 
# Python menggunakan urutan prioritas untuk menentukan operator mana yang dievaluasi terlebih dahulu. 
# Ini mirip dengan aturan matematika seperti "perkalian lebih dulu daripada penjumlahan".

# jadi sama halnya di matematika operator predence seperti kita saat mengerjakan sola matematik kita
# akan memperiritaskan perkalian pembagian seterlah itu baru pertambahan dan pengurangan

x = 12
y = 2
z = 6

operasi_predence = x + z / y * x // y  #kita bisa menambakan kurung untuk prioritas arimatika yang kita ingginkna
print(operasi_predence)





