# -Irfan di dalama bahasa pemograman python ada tipe data int alias angka satuan
data_integer = 1
print(type(data_integer)) #-Irfan ini adalah cara di dalama bahasa python jika ingin mengetahui type data apa di  varibel yang kita panggil
print("data :", data_integer, "adalah tipe data:", type(data_integer))


# tipe data float : angak dengan koma(float)
data_float = 1.2 # tipe data float sama aja kaya di flutter yaitu double 
print(type(data_float))

#tipe data string : kumpulan katakter  bahasa latin 
data_string = "irfan ganteng"
print(type(data_string))

#tipe data bollean = biner true atau flase (boplean)
data_bollean = True
print(type(data_bollean))

# tipe data complex tipe data yang mewakili bilangan kompleks. Bilangan kompleks terdiri dari bagian riil dan bagian imajiner.
data_complex = complex(12,4)
print(type(data_complex))
print(data_complex)

# didalam bahasa pemograman python kita bisa mengunakan tipe data yang ada di bahasa pemograman c
# caranya :

from ctypes import  c_double # kita bisa menambahakan lenih dari satu tipe data dari c
data_c_double = 10.5
print(type(data_c_double))
print(data_c_double)
