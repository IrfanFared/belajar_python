# for lop di dalam bahasa pemrograman python adalah perulangan yang digunakan untuk mengulang kode tertentu sebanyak n kali.
# konsep dasar dari for loop adalah kita akan melakukan perulangan sebanyak n kali, dan di dalam setiap perulangan tersebut kita akan melakukan sesuatu.
# untuk sytax dari for loop di python adalah sebagai berikut:
# for variable in sequence:
#     statement(s)
# variable adalah variabel yang akan diisi dengan elemen dari sequence secara berurutan.
# for kodisi:
    #angka

angka = [1, 2, 3, 4, 5]
for i in angka:
    print(i)


kelas = ["A", "B", "C", "D", "E"]
for i in kelas:
    print(f"Ada kelas {i}")

ulang = 10
for i in range(ulang):
    print(f"perulangan ke {i}")

data = "Saya cinta claaudia tapi ngak nyata"
for huruf in data:
    print(f"{huruf}")
