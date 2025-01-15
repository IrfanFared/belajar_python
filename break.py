# brak di dalam bahasa pemograman pythona adalah kata kunci yang digunakan untuk menghentikan perulangan.
# contoh penggunaan break dalam bahasa pemograman python adalah sebagai berikut:

angka = 0

while angka < 10:
    angka +=1
    print(f"perulangan ke {angka}")
    if angka == 5:
        print("angka 5 di print")
        break
    print("angka di print") # jadi jika kondi angka == 5 maka angka 5 tidak di print
print("progam selesai")