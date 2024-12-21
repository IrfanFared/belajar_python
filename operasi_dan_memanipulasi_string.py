# di dalama bahaa python kita bisa memnipulasi string 
# sting concatenate contoh

nama_depan = "Muhammad Irfan "
nama_belakang="pratama"

nama_lengkap = nama_depan + "" + nama_belakang #kamu bisa menambakan spass bisa gunakan string kosong
print(nama_lengkap)

# didalam python kita bisa mengitung ada berapa panjang string string
#contoh

panjang_string = len(nama_lengkap)
print(panjang_string)

#di dalam bahasa pemograman python kita bisa mengecek char atau string berasa di string atau tidak 
#contoh

string_i = "I"
cek_status_apakah_string_i_ada_di_variabelnamalengkap = string_i in nama_lengkap
print(cek_status_apakah_string_i_ada_di_variabelnamalengkap)

#negasi
string_x = "x"
cek_status_apakah_string_x_tidak_ada_di_variabelnamalengkap = string_i not in nama_lengkap
print(cek_status_apakah_string_x_tidak_ada_di_variabelnamalengkap)
 
#mengulang string yang sama
print("Violet istrinya Irfan\n"*12)