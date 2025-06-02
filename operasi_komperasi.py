# -Irfan di dalam python ada namanya operasi komperasi 
# -Irfan operasi komperasi tersediri  dalam python digunakan untuk  membandingakan  dua nilai yang memhasilkan  nilai boleann (true atau false )

# Operasi komparasi sederhana
a = 10
b = 20

print(a == b)  # False (sama dengan )
print(a != b)  # True (tidak sama dengan)
print(a > b)   # False (lebih dari)
print(a < b)   # True (kurang dari)
print(a >= 10) # True (lebih dari sama dengan)
print(b <= 15) # False (kurang dari sama dengan)

# -Irfan literal adalah representasi nilai varibel tetap 
#-irfan jadi terkadan ada yang membuat kita bingung yaiu operasi komparasi sama dengan denga is
#-jadi ada sebuah perbedaan dari keduanya 
print("variabel")
c = [1,2,3,4]
d = [1,2,3,4]
f = 1
e = 1

opeasi_sama_dengan = c == d #ini memeriksa apakah isi kedua variabel sama atau tidak
operaso_is = c is d #Membandingkan apakah dua variabel merujuk ke objek yang sama di memori
operaso_is_not = c is d #Membandingkan apakah dua variabel merujuk ke objek yang sama di memori
                    #Memeriksa apakah keduanya adalah objek yang identik

print(opeasi_sama_dengan)
print(operaso_is)
print(operaso_is_not)

#mencoba  mendapatkana alamat memori(addres) varibel 
# outpunya  alamat memori (addres) dari varibel akan sama tapi ada pengecualian Tipe Data Mutable (Seperti list, dict, set)
print(hex(id(f)))
print(hex(id(e)))

print(hex(id(c)))
print(hex(id(d)))

#Kata kunci hex dalam bahasa pemrograman Python adalah sebuah fungsi built-in yang digunakan untuk mengonversi angka bulat (integer) menjadi representasi string dalam format heksadesimal. Format heksadesimal adalah sistem bilangan berbasis 16 yang sering digunakan dalam pemrograman dan pengolahan data.